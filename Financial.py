# -*- coding: utf-8 -*-
import csv
import os
import random
import sqlite3
import time
from configparser import ConfigParser
from datetime import datetime

import pandas

import Constants
import DatabaseContract
import SinaFinancial
from BlackList import BlackList
from Favorite import Favorite
from FinancialData import FinancialData
from ShareBonus import ShareBonus
from Stock import Stock
from StockData import StockData

favorite_only = True
Favorite = Favorite()

check_black_list = True
black_list = BlackList()


def setup_database():
    connect = None

    print("setup_database")

    try:
        connect = sqlite3.connect(DatabaseContract.DATABASE_FILE_NAME)
        if connect is not None:
            cursor = connect.cursor()

            cursor.execute(DatabaseContract.SQL_CREATE_TABLE_STOCK)
            cursor.execute(DatabaseContract.SQL_CREATE_TABLE_STOCK_DATA)
            cursor.execute(DatabaseContract.SQL_CREATE_TABLE_FINANCIAL_DATA)
            cursor.execute(DatabaseContract.SQL_CREATE_TABLE_SHARE_BONUS)
            connect.commit()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()


def setup_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def make_data_directory():
    setup_directory(Constants.DATA_PATH)
    setup_directory(Constants.DATA_FINANCIAL_PATH)
    setup_directory(Constants.DATA_SHARE_BONUS_PATH)
    setup_directory(Constants.DATA_STOCK_PATH)
    setup_directory(Constants.DATA_STOCK_DAY_PATH)
    setup_directory(Constants.DATA_STOCK_WEEK_PATH)
    setup_directory(Constants.DATA_STOCK_MONTH_PATH)


def get_time_to_market(stock_data_list):
    time_to_market = None

    if stock_data_list is None:
        return time_to_market

    if stock_data_list is not None:
        time_to_market = stock_data_list[0]["date"]

    return time_to_market


def download():
    stock_tuple_list = read_stock_tuple_list_from_database()
    if stock_tuple_list is None:
        print("stock_tuple_list is None")
        return

    config = ConfigParser()
    config.read('config.ini')
    if not config.has_section("download"):
        config.add_section('download')
        config.set('download', 'index', "0")
        with open('config.ini', 'w') as f:
            config.write(f)

    index = int(config.get('download', 'index'))

    i = 0
    for stock_tuple in stock_tuple_list:
        i = i + 1
        if i < index:
            continue

        config.set('download', 'index', str(i))
        with open('config.ini', 'w') as f:
            config.write(f)

        stock = Stock(stock_tuple)
        if stock is None:
            continue

        if not check_out(stock):
            continue

        print(i, stock.mCode, stock.mName, stock.mMark, stock.mOperation)

        stock_data_list = download_stock_data(stock)

        time_to_market = get_time_to_market(stock_data_list)
        stock.set_time_to_market(time_to_market)

        # if stock.is_time_to_market_too_short():
        #     print("stock.is_time_to_market_too_short()")
        #     time.sleep(random.random() * 5)
        #     continue

        download_information_data(stock)

        download_financial_data(stock)

        download_share_bonus(stock)

        stock.update_to_database()

    config.set('download', 'index', "0")
    with open('config.ini', 'w') as f:
        config.write(f)

    print("download done")


def download_stock_list():
    page = 1
    stock_list = list()

    while page:
        result = SinaFinancial.SinaFinancial().download_stock_list(page)
        if result is None:
            break
        stock_list += result
        page += 1
        time.sleep(random.random())

    write_stock_list_to_database(stock_list)


def download_stock_data(stock):
    # stock_data_day_list = []
    # stock_data_week_list = []
    # stock_data_month_list = []

    if stock is None:
        return None

    sina = SinaFinancial.SinaFinancial()

    # stock_data_day_list = sina.download_stock_data(stock, -1, DAY)
    # write_stock_data_to_database(DAY, stock.mCode, stock_data_day_list)
    #
    # stock_data_week_list = sina.download_stock_data(stock, -1, WEEK)
    # write_stock_data_to_database(WEEK, stock.mCode, stock_data_week_list)

    stock_data_month_list = sina.download_stock_data(stock, -1)
    write_stock_data_to_database(stock.mCode, stock_data_month_list)

    return stock_data_month_list


def download_information_data(stock):
    if stock is None:
        return None

    sina = SinaFinancial.SinaFinancial()

    information_data_list = sina.download_stock_information(stock)

    if information_data_list is not None:
        string = information_data_list[0]
        if string is not None:
            words = string.split("\"")
            if len(words) == 2:
                stock.set_classes(words[1])
        stock.set_pinyin(information_data_list[1])
        stock.set_total_share(int(float(information_data_list[7]) * Constants.DOUBLE_CONSTANT_WAN))

    return information_data_list


def download_financial_data(stock):
    if stock is None:
        return None

    sina = SinaFinancial.SinaFinancial()

    financial_data_list = sina.download_financial_data(stock)

    if financial_data_list is None:
        print("download_financial_data", "download_financial_data is None, return")
        return

    write_financial_data_to_database(stock.mCode, financial_data_list)

    return financial_data_list[::-1]


def download_share_bonus(stock):
    if stock is None:
        return None

    sina = SinaFinancial.SinaFinancial()

    share_bonus_list = sina.download_share_bonus(stock)

    write_share_bonus_to_database(stock.mCode, share_bonus_list)

    return share_bonus_list


def write_stock_list_to_database(stock_list):
    connect = None
    executemany = False
    insert_tuple_list = []

    query_sql = Stock.get_query_sql()
    insert_sql = Stock.get_insert_sql()
    update_sql = Stock.get_update_sql()

    print("write_stock_list_to_database")

    if stock_list is None:
        print("stock_list is None, return")
        return

    if len(stock_list) == 0:
        print("stock_list len =", len(stock_list), ", return")
        return

    try:
        connect = sqlite3.connect(DatabaseContract.DATABASE_FILE_NAME)
        cursor = connect.cursor()

        cursor.execute(query_sql)
        if cursor.fetchone() is None:
            executemany = True

        for stock_basic in stock_list:
            stock = Stock(stock_basic)

            if not check_out(stock):
                continue

            now = datetime.now().strftime(Constants.DATE_TIME_FORMAT)

            if executemany:
                stock.set_created(now)
                stock.set_modified(now)

                insert_tuple = stock.get_insert_tuple()
                insert_tuple_list.append(insert_tuple)
            else:
                sql_check_record_exist = Stock.get_query_sql("code=?")
                cursor.execute(sql_check_record_exist, (stock.mCode,))
                stock_tuple = cursor.fetchone()
                if stock_tuple is None:
                    stock.set_created(now)
                    stock.set_modified(now)

                    insert_tuple = stock.get_insert_tuple()

                    cursor.execute(insert_sql, insert_tuple)
                    connect.commit()
                    print("write_stock_list_to_database, insert stock:", insert_tuple)
                else:
                    stock.set_modified(now)

                    update_tuple = stock.get_update_tuple()

                    cursor.execute(update_sql, update_tuple)
                    connect.commit()
                    print("write_stock_list_to_database, update stock:", update_tuple)
        if executemany:
            print("insert: executemany")
            cursor.executemany(insert_sql, insert_tuple_list)
            connect.commit()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()


def write_stock_data_to_database(code, stock_data_list, period=Constants.MONTH):
    connect = None
    record_list = []

    sql_delete = "DELETE FROM stock_data WHERE period = ? AND stock_code = ?"
    sql_insert = "INSERT INTO stock_data (stock_code, date, time, period," \
                 " open, high, low, close, volume," \
                 " created, modified)" \
                 " VALUES(?,?,?,?,?,?,?,?,?,?,?)"

    # print("write_stock_data_to_database period=", period, " code=", code)

    if stock_data_list is None:
        print("stock_data_list is None, return")
        return

    try:
        connect = sqlite3.connect(DatabaseContract.DATABASE_FILE_NAME)
        cursor = connect.cursor()

        cursor.execute(sql_delete, (period, code))

        index = -1
        for stock_data in stock_data_list:
            index = index + 1

            date = stock_data['date']
            open = stock_data['open']
            high = stock_data['high']
            low = stock_data['low']
            close = stock_data['close']
            volume = stock_data['volume']

            time = "00:00"
            now = datetime.now().strftime(Constants.DATE_TIME_FORMAT)

            record = tuple((code, date, time, period, open, high, low, close, volume, now, now))
            record_list.append(record)

        cursor.executemany(sql_insert, record_list)
        connect.commit()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()


def write_financial_data_to_database(code, financial_data_list):
    connect = None
    record_list = []

    sql_delete = "DELETE FROM financial_data WHERE stock_code = ?"
    sql_insert = "INSERT INTO financial_data (stock_code, date," \
                 "book_value_per_share, cash_flow_per_share, total_current_assets," \
                 "total_assets, total_long_term_liabilities, main_business_income," \
                 "financial_expenses, net_profit, net_profit_per_share," \
                 "created, modified)" \
                 " VALUES(?,?," \
                 "?,?,?," \
                 "?,?,?," \
                 "?,?,?," \
                 "?,?)"

    if financial_data_list is None:
        print("financial_data_list is None, return")
        return

    try:
        connect = sqlite3.connect(DatabaseContract.DATABASE_FILE_NAME)
        cursor = connect.cursor()

        cursor.execute(sql_delete, (code,))

        index = -1
        for financial_data in financial_data_list:
            index = index + 1

            date = financial_data['date']
            book_value_per_share = financial_data['book_value_per_share']
            cash_flow_per_share = financial_data['cash_flow_per_share']
            total_current_assets = financial_data['total_current_assets']
            total_assets = financial_data['total_assets']
            total_long_term_liabilities = financial_data['total_long_term_liabilities']
            main_business_income = financial_data['main_business_income']
            financial_expenses = financial_data['financial_expenses']
            net_profit = financial_data['net_profit']
            net_profit_per_share = financial_data['net_profit_per_share']

            now = datetime.now().strftime(Constants.DATE_TIME_FORMAT)

            record = tuple((code, date, book_value_per_share, cash_flow_per_share,
                            total_current_assets, total_assets, total_long_term_liabilities,
                            main_business_income, financial_expenses, net_profit, net_profit_per_share,
                            now, now))
            record_list.append(record)

        cursor.executemany(sql_insert, record_list)
        connect.commit()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()


def write_share_bonus_to_database(code, share_bonus_list):
    connect = None
    record_list = []

    sql_delete = "DELETE FROM share_bonus WHERE stock_code = ?"
    sql_insert = "INSERT INTO share_bonus (stock_code, date, " \
                 "dividend, r_date, " \
                 "created, modified)" \
                 " VALUES(?,?," \
                 "?,?," \
                 "?,?)"

    if share_bonus_list is None:
        print("share_bonus_list is None, return")
        return

    try:
        connect = sqlite3.connect(DatabaseContract.DATABASE_FILE_NAME)
        cursor = connect.cursor()

        cursor.execute(sql_delete, (code,))

        index = -1
        for share_bonus in share_bonus_list:
            index = index + 1

            date = share_bonus['date']
            dividend = share_bonus['dividend']
            r_date = share_bonus['r_date']

            now = datetime.now().strftime(Constants.DATE_TIME_FORMAT)

            record = tuple((code, date, dividend, r_date,
                            now, now))
            record_list.append(record)

        cursor.executemany(sql_insert, record_list)
        connect.commit()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()


def get_stock_file_name():
    return "./data/stock/stock.csv"


def get_stock_data_file_name(stock, period=Constants.MONTH):
    if stock is None:
        return None
    else:
        return "./data/stock/" + period + "/" + stock.mCode + ".csv"


def get_financial_data_file_name(stock):
    if stock is None:
        return None
    else:
        return "./data/financial/" + stock.mCode + ".csv"


def get_share_bonus_file_name(stock):
    if stock is None:
        return None
    else:
        return "./data/share_bonus/" + stock.mCode + ".csv"


def get_value_string_by_key(key, dictionary):
    value = 0.0

    if key in dictionary:
        value = dictionary[key]

    return str(value)


def read_stock_from_file():
    file_name = get_stock_file_name()

    stocks = pandas.read_csv(file_name, sep='\t', engine='python')
    if stocks is None:
        return None

    stock_list = map(list, stocks.values)

    for stock_item in stock_list:
        ttt = tuple(str(stock_item).split(", "))
        stock = Stock(ttt)
        print(stock)

    return stocks


def write_stock_to_file(stock_tuple_list):
    if stock_tuple_list is None:
        return

    if len(stock_tuple_list) == 0:
        return

    file_name = get_stock_file_name()

    field_name_tuple = tuple(("id", "classes", "se", "code",
                              "name", "pinyin", "mark", "price",
                              "change", "net", "volume", "value",
                              "operation", "hold", "cost", "profit",
                              "total_share", "roe", "rate", "valuation",
                              "discount", "pe", "pb", "dividend",
                              "dividend_yield", "delta", "time_to_market",
                              "created", "modified"))

    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name_tuple)
        writer.writeheader()

        for stock_tuple in stock_tuple_list:
            stock = Stock(stock_tuple)
            if stock is None:
                continue

            stock_dict = {"id": stock.mID, "classes": stock.mClasses, "se": stock.mSE, "code": stock.mCode,
                          "name": stock.mName, "pinyin": stock.mPinyin, "mark": stock.mMark, "price": stock.mPrice,
                          "change": stock.mChange, "net": stock.mNet, "volume": stock.mVolume, "value": stock.mValue,
                          "operation": stock.mOperation, "hold": stock.mHold, "cost": stock.mCost, "profit": stock.mProfit,
                          "total_share": stock.mTotalShare, "roe": stock.mRoe, "rate": stock.mRate,
                          "pe": stock.mPe, "pb": stock.mPb, "dividend": stock.mDividend,
                          "dividend_yield": stock.mDividendYield, "delta": stock.mDelta,
                          "time_to_market": stock.mTimeToMarket,
                          "created": stock.mCreated, "modified": stock.mModified}
            writer.writerow(stock_dict)


def write_stock_data_to_file(stock, stock_data_tuple_list, period=Constants.MONTH):
    if stock is None:
        return

    if stock_data_tuple_list is None:
        return

    if len(stock_data_tuple_list) == 0:
        return

    file_name = get_stock_data_file_name(stock, period)

    field_name_tuple = tuple(("date", "open", "high", "low", "close", "volume"))

    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name_tuple)
        writer.writeheader()

        for stock_data_tuple in stock_data_tuple_list:
            stock_data = StockData(stock_data_tuple)
            if stock_data is None:
                continue

            stock_data_dict = {"date": stock_data.date, "open": stock_data.open, "high": stock_data.high,
                               "low": stock_data.low, "close": stock_data.close, "volume": stock_data.volume}
            writer.writerow(stock_data_dict)


def write_financial_data_to_file(stock, financial_data_tuple_list):
    if stock is None:
        return

    if financial_data_tuple_list is None:
        return

    if len(financial_data_tuple_list) == 0:
        return

    file_name = get_financial_data_file_name(stock)

    field_name_tuple = tuple(("date",
                              "book_value_per_share",
                              "cash_flow_per_share",
                              "total_current_assets",
                              "total_assets",
                              "total_long_term_liabilities",
                              "main_business_income",
                              "financial_expenses",
                              "net_profit",
                              "net_profit_per_share"))

    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name_tuple)
        writer.writeheader()

        for financial_data_tuple in financial_data_tuple_list:
            financial_data = FinancialData(financial_data_tuple)
            if financial_data is None:
                continue

            financial_data_dict = {"date": financial_data.date,
                                   "book_value_per_share": financial_data.book_value_per_share,
                                   "cash_flow_per_share": financial_data.cash_flow_per_share,
                                   "total_current_assets": financial_data.total_current_assets,
                                   "total_assets": financial_data.total_assets,
                                   "total_long_term_liabilities": financial_data.total_long_term_liabilities,
                                   "main_business_income": financial_data.main_business_income,
                                   "financial_expenses": financial_data.financial_expenses,
                                   "net_profit": financial_data.net_profit,
                                   "net_profit_per_share": financial_data.net_profit_per_share,
                                   }
            writer.writerow(financial_data_dict)


def write_share_bonus_to_file(stock, share_bonus_tuple_list):
    if stock is None:
        return

    if share_bonus_tuple_list is None:
        return

    if len(share_bonus_tuple_list) == 0:
        return

    file_name = get_share_bonus_file_name(stock)

    field_name_tuple = tuple(("date",
                              "dividend",
                              "r_date"))

    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name_tuple)
        writer.writeheader()

        for share_bonus_tuple in share_bonus_tuple_list:
            share_bonus = ShareBonus(share_bonus_tuple)
            if share_bonus is None:
                continue

            share_bonus_dict = {"date": share_bonus.date,
                                "dividend": share_bonus.dividend,
                                "r_date": share_bonus.r_date,
                                }
            writer.writerow(share_bonus_dict)


#
# def read_stock_tuple_from_database(code):
#     connect = None
#     stock_tuple = tuple()
#
#     sql_query = "SELECT * FROM stock WHERE code = ?"
#
#     try:
#         connect = sqlite3.connect(database_contract.DATABASE_FILE_NAME)
#         cursor = connect.cursor()
#         cursor.execute(sql_query, (code,))
#         stock_tuple = cursor.fetchone()
#     except sqlite3.Error as e:
#         print('e:', e)
#     finally:
#         if connect is not None:
#             connect.close()
#
#     return stock_tuple


def read_stock_tuple_list_from_database(where=None, order=None, sort=None):
    connect = None
    stock_tuple_list = tuple()

    sql_query = Stock.get_query_sql(where, order, sort)

    try:
        connect = sqlite3.connect(DatabaseContract.DATABASE_FILE_NAME)
        cursor = connect.cursor()
        cursor.execute(sql_query)
        stock_tuple_list = cursor.fetchall()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()

    return stock_tuple_list


def read_stock_data_from_database(stock, period=Constants.MONTH):
    connect = None
    sql_query = "SELECT * FROM stock_data WHERE stock_code = ? AND period = ?  order by date desc"
    stock_data_tuple_list = tuple()

    if stock is None:
        return None

    try:
        connect = sqlite3.connect(DatabaseContract.DATABASE_FILE_NAME)
        cursor = connect.cursor()
        cursor.execute(sql_query, (stock.mCode, period))
        stock_data_tuple_list = cursor.fetchall()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()

    return stock_data_tuple_list


def analyze_stock_data(stock, stock_data_tuple_list, financial_data_tuple_list):
    if stock is None:
        return stock

    if stock_data_tuple_list is None:
        return stock

    if len(stock_data_tuple_list) < 1:
        return stock

    if financial_data_tuple_list is None:
        return stock

    if len(financial_data_tuple_list) < 1:
        return stock

    stock_data_tuple = stock_data_tuple_list[0]
    financial_data_tuple = financial_data_tuple_list[0]

    stock_data = StockData(stock_data_tuple)
    if stock_data is None:
        return stock

    financial_data = FinancialData(financial_data_tuple)
    if financial_data is None:
        return stock

    if stock.dividend != 0:
        stock.delta = round(financial_data.net_profit_per_share / (stock.dividend / 10.0), 2)

    if financial_data.net_profit_per_share != 0:
        stock.valuation = financial_data.net_profit_per_share / Constants.RISK_INTEREST_RATE
        if stock.valuation != 0:
            stock.discount = round(stock.price / stock.valuation, 2)

        if stock.price != 0:
            stock.pe = round(100.0 * financial_data.net_profit_per_share / stock.price, 2)

    book_value_per_share = financial_data.book_value_per_share
    if book_value_per_share != 0:
        stock.pb = round(stock.price / book_value_per_share, 2)
        stock.roe = round(100.0 * financial_data.net_profit_per_share / book_value_per_share, 2)

    # if (0 < stock.pe < constant.PE_MAX) and (0 < stock.pb < constant.PB_MAX):
    #     stock.operation |= constant.PRICE_TYPE

    if financial_data.total_long_term_liabilities < financial_data.main_business_income:
        stock.operation |= Constants.LIABILITIES_TYPE

    return stock


def read_financial_data_from_database(stock):
    connect = None
    financial_data_tuple_list = tuple()
    sql_query = "SELECT * FROM financial_data WHERE stock_code = ?  order by date desc"
    if stock is None:
        return None

    try:
        connect = sqlite3.connect(DatabaseContract.DATABASE_FILE_NAME)
        cursor = connect.cursor()
        cursor.execute(sql_query, (stock.mCode,))
        financial_data_tuple_list = cursor.fetchall()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()

    return financial_data_tuple_list


def read_share_bonus_from_database(stock):
    connect = None
    share_bonus_tuple_list = tuple()
    sql_query = "SELECT * FROM share_bonus WHERE stock_code = ?  order by date desc"
    if stock is None:
        return None

    try:
        connect = sqlite3.connect(DatabaseContract.DATABASE_FILE_NAME)
        cursor = connect.cursor()
        cursor.execute(sql_query, (stock.mCode,))
        share_bonus_tuple_list = cursor.fetchall()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()

    return share_bonus_tuple_list


def analyze_financial_data(stock, financial_data_tuple_list):
    if stock is None:
        return stock

    if financial_data_tuple_list is None:
        return stock

    if len(financial_data_tuple_list) < 2 * Constants.SEASONS_IN_A_YEAR + 1:
        return stock

    financial_data = FinancialData(financial_data_tuple_list[0])
    if financial_data is None:
        return stock

    stock.set_total_assets(financial_data.total_assets)
    stock.set_total_long_term_liabilities(financial_data.total_long_term_liabilities)
    stock.set_book_value_per_share(financial_data.book_value_per_share)
    stock.set_cash_flow_per_share(financial_data.cash_flow_per_share)
    stock.set_net_profit(financial_data.net_profit)

    stock.setup_net_profit_per_share()
    stock.setup_net_profit_per_share_in_year(financial_data_tuple_list)
    stock.setup_net_profit_per_share_last_year(financial_data_tuple_list)
    stock.setup_rate()
    stock.setup_debt_to_net_assets_rato()
    stock.setup_roe(financial_data_tuple_list)
    stock.setup_pe()
    stock.setup_pb()

    return stock


def analyze_share_bonus(stock, share_bonus_tuple_list):
    total_divident = 0
    prev_year = None

    if stock is None:
        return stock

    if share_bonus_tuple_list is None:
        return stock

    index = -1
    for share_bonus_tuple in share_bonus_tuple_list:
        index = index + 1

        if share_bonus_tuple is None:
            break

        share_bonus = ShareBonus(share_bonus_tuple)
        if share_bonus is None:
            break

        if share_bonus.date is None:
            break

        strings = share_bonus.date.split("-")

        if strings is None or len(strings) == 0:
            break

        year = strings[0]

        if prev_year is not None:
            if prev_year != year:
                break

        total_divident += float(share_bonus.dividend)

        if index == 0:
            stock.set_date(share_bonus.date)
            stock.set_r_date(share_bonus.r_date)

        stock.set_dividend(round(total_divident, Constants.DOUBLE_FIXED_DECIMAL))
        stock.setup_dividend_yield()
        stock.setup_delta()

        prev_year = year

    return stock

def analyze():
    stock_tuple_list = read_stock_tuple_list_from_database()

    count = 0
    index = -1
    for stock_tuple in stock_tuple_list:
        index = index + 1
        if index < 0:
            continue

        stock = Stock(stock_tuple)
        if stock is None:
            continue

        if not check_out(stock):
            continue

        count += 1

        print(index, stock.mCode, stock.mName, stock.mMark, stock.mOperation)

        stock_data_tuple_list = read_stock_data_from_database(stock)
        financial_data_tuple_list = read_financial_data_from_database(stock)
        share_bonus_tuple_list = read_share_bonus_from_database(stock)

        stock = analyze_financial_data(stock, financial_data_tuple_list)
        stock = analyze_share_bonus(stock, share_bonus_tuple_list)
        # stock = analyze_stock_data(stock, stock_data_tuple_list, financial_data_tuple_list)

        stock.update_to_database()

    print("analyze done, count=", count)


def select(where=None, order=None, sort=None):
    select_tuple_list = tuple()

    make_data_directory()

    stock_tuple_list = read_stock_tuple_list_from_database(where, order, sort)
    write_stock_to_file(stock_tuple_list)

    for stock_tuple in stock_tuple_list:
        stock = Stock(stock_tuple)

        if not check_out(stock):
            continue

        print("\"" + stock.mCode + "\"" + ", #" + stock.mName + " "
              + "roe " + str(stock.mRoe) + " "
              + "pe " + str(stock.mPe) + " pb " + str(stock.mPb) + " "
              + "dividend " + str(stock.mDividend) + " " + str(stock.mDividendYield) + "% "
              + " operation " + str(stock.mOperation))

    print("select done, count=", len(stock_tuple_list))

    return stock_tuple_list


def write_to_file(stock):
    if stock is None:
        return

    stock_data_tuple_list = read_stock_data_from_database(stock)
    write_stock_data_to_file(stock, stock_data_tuple_list)

    financial_data_tuple_list = read_financial_data_from_database(stock)
    write_financial_data_to_file(stock, financial_data_tuple_list)

    share_bonus_tuple_list = read_share_bonus_from_database(stock)
    write_share_bonus_to_file(stock, share_bonus_tuple_list)


def update_mark():
    stock_tuple_list = read_stock_tuple_list_from_database()

    black_stock_list = black_list.get_stock_list()
    if black_stock_list is None:
        return

    favorite_stock_list = Favorite.get_stock_list()
    if favorite_stock_list is None:
        return

    count = 0
    index = -1
    for stock_tuple in stock_tuple_list:
        index = index + 1
        if index < 0:
            continue

        stock = Stock(stock_tuple)
        if stock is None:
            continue

        stock.set_mark(Constants.STOCK_TYPE_NONE)

        if stock.mCode in favorite_stock_list:
            stock.set_mark(Constants.STOCK_TYPE_FAVORITE)

        if stock.mCode in black_stock_list:
            stock.set_mark(Constants.STOCK_TYPE_BLACK)

        stock.update_to_database()
        count += 1

        print(index, stock.mCode, stock.mName, stock.mOperation, stock.mMark, stock.mDiscount)

    print("update done, count=", count)


def in_favorite_list(stock):
    result = False

    favorite_stock_list = Favorite.get_stock_list()
    if favorite_stock_list is None:
        return result

    if stock.mCode in favorite_stock_list:
        result = True

    return result


def in_black_list(stock):
    result = False

    black_stock_list = black_list.get_stock_list()
    if black_stock_list is None:
        return result

    if not check_black_list:
        return result

    if stock.mCode in black_stock_list:
        result = True

    return result


def check_out(stock):
    result = False

    if favorite_only:
        return in_favorite_list(stock)
    else:
        if stock.is_special_treatment():
            return False
        elif stock.mPe < 0:
            return False
        elif stock.mPb < 0:
            return False
        elif stock.is_time_to_market_too_short():
            return False
        elif in_black_list(stock):
            return False
        else:
            result = True

    return result
