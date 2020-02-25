# -*- coding: utf-8 -*-
import pandas
from dateutil.relativedelta import relativedelta

import constant
import csv
import os
import sina_financial
import sqlite3
import time
import random

import database_contract
import black
import favorite

from datetime import datetime

favorite_only = False


def setup_database():
    connect = None

    print("setup_database")

    try:
        connect = sqlite3.connect(database_contract.DATABASE_FILE_NAME)
        if connect is not None:
            cursor = connect.cursor()

            cursor.execute(database_contract.SQL_CREATE_TABLE_STOCK)
            cursor.execute(database_contract.SQL_CREATE_TABLE_STOCK_DATA)
            cursor.execute(database_contract.SQL_CREATE_TABLE_FINANCIAL_DATA)
            cursor.execute(database_contract.SQL_CREATE_TABLE_SHARE_BONUS)
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
    setup_directory(constant.DATA_PATH)
    setup_directory(constant.DATA_FINANCIAL_PATH)
    setup_directory(constant.DATA_SHARE_BONUS_PATH)
    setup_directory(constant.DATA_STOCK_PATH)
    setup_directory(constant.DATA_STOCK_DAY_PATH)
    setup_directory(constant.DATA_STOCK_WEEK_PATH)
    setup_directory(constant.DATA_STOCK_MONTH_PATH)


def get_time_to_market(stock_data_list):
    time_to_market = None

    if stock_data_list is None:
        return time_to_market

    if stock_data_list is not None:
        time_to_market = stock_data_list[0]["date"]

    return time_to_market


def download():
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

        # if not stock.check_out():
        #     continue

        count += 1

        print(index, stock.code, stock.name, stock.mark, stock.operation)

        stock_data_list = download_stock_data(stock)

        time_to_market = get_time_to_market(stock_data_list)
        stock.set_time_to_market(time_to_market)

        if stock.is_time_to_market_too_short():
            time.sleep(random.random())
            print("stock.is_time_to_market_too_short()")

        download_information_data(stock)

        download_financial_data(stock)

        download_share_bonus(stock)

        stock.update_to_database()

    print("download done, count=", count)


def download_stock_list():
    page = 1
    stock_list = list()

    while page:
        result = sina_financial.SinaFinancial().download_stock_list(page)
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

    sina = sina_financial.SinaFinancial()

    # print("download_stock_data code=", stock.code)

    # stock_data_day_list = sina.download_stock_data(stock.code, -1, DAY)
    # write_stock_data_to_database(DAY, stock.code, stock_data_day_list)
    #
    # stock_data_week_list = sina.download_stock_data(stock.code, -1, WEEK)
    # write_stock_data_to_database(WEEK, stock.code, stock_data_week_list)

    stock_data_month_list = sina.download_stock_data(stock.code, -1)
    write_stock_data_to_database(stock.code, stock_data_month_list)

    return stock_data_month_list


def download_information_data(stock):
    information_data_list = []

    if stock is None:
        return None

    sina = sina_financial.SinaFinancial()

    information_data_list = sina.download_stock_information(stock.code)

    if information_data_list is not None:
        string = information_data_list[0]
        if string is not None:
            words = string.split("\"")
            if len(words) == 2:
                stock.set_classes(words[1])
        stock.set_pinyin(information_data_list[1])
        stock.set_total_share(int(float(information_data_list[7]) * 10000))

    return information_data_list


def download_financial_data(stock):
    time_to_market_len_min = constant.TIME_TO_MARKET_YEAR_MIN * constant.SEASONS_IN_A_YEAR

    # book_value_per_share = {}
    # cash_flow_per_share = {}
    # total_current_assets = {}
    # total_assets = {}
    # total_long_term_liabilities = {}
    # main_business_income = {}
    # financial_expenses = {}
    # net_profit = {}

    financial_data_list = []
    # test_financial_data_list = []

    if stock is None:
        return None

    sina = sina_financial.SinaFinancial()

    # print("download_financial_data code=", stock.code)

    # book_value_per_share = sina.download_financial_data(stock.code, 'mgjzc')
    # cash_flow_per_share = sina.download_financial_data(stock.code, 'mgxjhl')
    # total_current_assets = sina.download_financial_data(stock.code, 'ldzchj')
    # total_assets = sina.download_financial_data(stock.code, 'zczj')
    # total_long_term_liabilities = sina.download_financial_data(stock.code, 'cqfzhj')
    # main_business_income = sina.download_financial_data(stock.code, 'zyywsr')
    # financial_expenses = sina.download_financial_data(stock.code, 'cwfy')
    # net_profit = sina.download_financial_data(stock.code, 'jlr')
    #
    # for key in sorted(book_value_per_share.keys()):
    #     if key is None:
    #         continue
    #
    #     if not_before is not None:
    #         if datetime.strptime(key, constant.DATE_FORMAT) < not_before:
    #             continue
    #
    #     financial_data = dict()
    #     financial_data["date"] = key
    #     financial_data["book_value_per_share"] = get_value_string_by_key(key, book_value_per_share)
    #     financial_data["cash_flow_per_share"] = get_value_string_by_key(key, cash_flow_per_share)
    #     financial_data["total_current_assets"] = get_value_string_by_key(key, total_current_assets)
    #     financial_data["total_assets"] = get_value_string_by_key(key, total_assets)
    #     financial_data["total_long_term_liabilities"] = get_value_string_by_key(key, total_long_term_liabilities)
    #     financial_data["main_business_income"] = get_value_string_by_key(key, main_business_income)
    #     financial_data["financial_expenses"] = get_value_string_by_key(key, financial_expenses)
    #     financial_data["net_profit"] = get_value_string_by_key(key, net_profit)
    #
    #     net_assets = float(financial_data["total_assets"]) - float(financial_data["total_long_term_liabilities"])
    #     if net_assets == 0:
    #         financial_data["roe"] = 0
    #     else:
    #         financial_data["roe"] = 100.0 * float(financial_data["net_profit"]) / float(net_assets)
    #
    #     financial_data["book_value_per_share_rate"] = financial_data["book_value_per_share"]
    #
    #     financial_data_list.append(financial_data)

    financial_data_list = sina.download_financial_data(stock)

    # list_len = len(financial_data_list)
    # if list_len > time_to_market_len_min:
    #     begin = financial_data_list[list_len - time_to_market_len_min - 1]
    #     end = financial_data_list[list_len - 1]
    #
    #     value0 = float(begin["book_value_per_share"])
    #     value1 = float(end["book_value_per_share"])
    #
    #     index = 0
    #     for financial_data in financial_data_list:
    #         if index < list_len - time_to_market_len_min - 1:
    #             test_financial_data_list.append(financial_data)
    #         else:
    #             financial_data["book_value_per_share_rate"] = value0 + (index - (list_len - time_to_market_len_min - 1)) * (value1 - value0) / time_to_market_len_min
    #             test_financial_data_list.append(financial_data)
    #         index += 1
    #     write_financial_data_to_database(stock.code, test_financial_data_list)
    #     return test_financial_data_list
    # else:
    #     write_financial_data_to_database(stock.code, financial_data_list)
    #     return financial_data_list

    write_financial_data_to_database(stock.code, financial_data_list)

    return financial_data_list[::-1]


def download_share_bonus(stock):
    if stock is None:
        return None

    sina = sina_financial.SinaFinancial()

    share_bonus_list = sina.download_share_bonus(stock.code)

    write_share_bonus_to_database(stock.code, share_bonus_list)

    return share_bonus_list


def write_stock_list_to_database(stock_list):
    connect = None
    executemany = False
    insert_tuple_list = []

    query_sql = Stock.get_query_sql()
    insert_sql = Stock.get_insert_sql()

    print("write_stock_list_to_database")

    if stock_list is None:
        print("stock_list is None, return")
        return

    try:
        connect = sqlite3.connect(database_contract.DATABASE_FILE_NAME)
        cursor = connect.cursor()

        cursor.execute(query_sql)
        if cursor.fetchone() is None:
            executemany = True

        for stock_basic in stock_list:
            stock = Stock(stock_basic)

            # if not stock.check_out():
            #     continue

            now = datetime.now().strftime(constant.DATE_TIME_FORMAT)

            if executemany:
                stock.set_created(now)
                stock.set_modified(now)

                insert_tuple = stock.get_insert_tuple()
                insert_tuple_list.append(insert_tuple)
            else:
                sql_check_record_exist = Stock.get_query_sql("code=?")
                cursor.execute(sql_check_record_exist, (stock.code,))
                stock_tuple = cursor.fetchone()
                if stock_tuple is None:
                    stock.set_created(now)
                    stock.set_modified(now)

                    insert_tuple = stock.get_insert_tuple()

                    cursor.execute(insert_sql, insert_tuple)
                    connect.commit()
                    print("insert stock:", insert_tuple)
                else:
                    stock.set_modified(now)

                    update_sql = Stock.get_update_sql()
                    update_tuple = stock.get_update_tuple()

                    cursor.execute(update_sql, update_tuple)
                    connect.commit()
                    print("update stock:", update_tuple)
        if executemany:
            print("insert: executemany")
            cursor.executemany(insert_sql, insert_tuple_list)
            connect.commit()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()


def write_stock_data_to_database(code, stock_data_list, period=constant.MONTH):
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
        connect = sqlite3.connect(database_contract.DATABASE_FILE_NAME)
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
            now = datetime.now().strftime(constant.DATE_TIME_FORMAT)

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
        connect = sqlite3.connect(database_contract.DATABASE_FILE_NAME)
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

            now = datetime.now().strftime(constant.DATE_TIME_FORMAT)

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
                 "dividend, dividend_date, " \
                 "created, modified)" \
                 " VALUES(?,?," \
                 "?,?," \
                 "?,?)"

    if share_bonus_list is None:
        print("share_bonus_list is None, return")
        return

    try:
        connect = sqlite3.connect(database_contract.DATABASE_FILE_NAME)
        cursor = connect.cursor()

        cursor.execute(sql_delete, (code,))

        index = -1
        for share_bonus in share_bonus_list:
            index = index + 1

            date = share_bonus['date']
            dividend = share_bonus['dividend']
            dividend_date = share_bonus['dividend_date']

            now = datetime.now().strftime(constant.DATE_TIME_FORMAT)

            record = tuple((code, date, dividend, dividend_date,
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


def get_stock_data_file_name(stock, period=constant.MONTH):
    if stock is None:
        return None
    else:
        return "./data/stock/" + period + "/" + stock.code + ".csv"


def get_financial_data_file_name(stock):
    if stock is None:
        return None
    else:
        return "./data/financial/" + stock.code + ".csv"


def get_share_bonus_file_name(stock):
    if stock is None:
        return None
    else:
        return "./data/share_bonus/" + stock.code + ".csv"


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

            stock_dict = {"id": stock.id, "classes": stock.classes, "se": stock.se, "code": stock.code,
                          "name": stock.name, "pinyin": stock.pinyin, "mark": stock.mark, "price": stock.price,
                          "change": stock.change, "net": stock.net, "volume": stock.volume, "value": stock.value,
                          "operation": stock.operation, "hold": stock.hold, "cost": stock.cost, "profit": stock.profit,
                          "total_share": stock.total_share, "roe": stock.roe, "rate": stock.rate, "valuation": stock.valuation,
                          "discount": stock.discount, "pe": stock.pe, "pb": stock.pb, "dividend": stock.dividend,
                          "dividend_yield": stock.dividend_yield, "delta": stock.delta, "time_to_market": stock.time_to_market,
                          "created": stock.created, "modified": stock.modified}
            writer.writerow(stock_dict)


def write_stock_data_to_file(stock, stock_data_tuple_list, period=constant.MONTH):
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
                              "dividend_date"))

    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name_tuple)
        writer.writeheader()

        for share_bonus_tuple in share_bonus_tuple_list:
            share_bonus = ShareBonus(share_bonus_tuple)
            if share_bonus is None:
                continue

            share_bonus_dict = {"date": share_bonus.date,
                                "dividend": share_bonus.dividend,
                                "dividend_date": share_bonus.dividend_date,
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
        connect = sqlite3.connect(database_contract.DATABASE_FILE_NAME)
        cursor = connect.cursor()
        cursor.execute(sql_query)
        stock_tuple_list = cursor.fetchall()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()

    return stock_tuple_list


def read_stock_data_from_database(stock, period=constant.MONTH):
    connect = None
    sql_query = "SELECT * FROM stock_data WHERE stock_code = ? AND period = ?  order by date desc"
    stock_data_tuple_list = tuple()

    if stock is None:
        return None

    try:
        connect = sqlite3.connect(database_contract.DATABASE_FILE_NAME)
        cursor = connect.cursor()
        cursor.execute(sql_query, (stock.code, period))
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
        stock.valuation = financial_data.net_profit_per_share / constant.RISK_INTEREST_RATE
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
        stock.operation |= constant.LIABILITIES_TYPE

    return stock


def read_financial_data_from_database(stock):
    connect = None
    financial_data_tuple_list = tuple()
    sql_query = "SELECT * FROM financial_data WHERE stock_code = ?  order by date desc"
    if stock is None:
        return None

    try:
        connect = sqlite3.connect(database_contract.DATABASE_FILE_NAME)
        cursor = connect.cursor()
        cursor.execute(sql_query, (stock.code,))
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
        connect = sqlite3.connect(database_contract.DATABASE_FILE_NAME)
        cursor = connect.cursor()
        cursor.execute(sql_query, (stock.code,))
        share_bonus_tuple_list = cursor.fetchall()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()

    return share_bonus_tuple_list


def analyze_growth(data_list):
    result = 0

    if len(data_list) < constant.GROWTH_YEAR_MIN:
        return result

    last = data_list[0]
    for data in data_list:
        if data > last:
            return result
        last = data

    result = 1

    return result


def analyze_growth2(data_list_q1, data_list_q4):
    result = 0

    if analyze_growth(data_list_q1) and analyze_growth(data_list_q4):
        result = 1

    return result


def analyze_financial_data(stock, financial_data_tuple_list):
    growth_year_min = constant.GROWTH_YEAR_MIN - 1
    time_to_market_len_min = constant.TIME_TO_MARKET_YEAR_MIN * constant.SEASONS_IN_A_YEAR
    base = 0
    target = 0;

    if stock is None:
        return stock

    if financial_data_tuple_list is None:
        return stock

    if len(financial_data_tuple_list) < time_to_market_len_min:
        return stock

    main_business_income_q1 = []
    main_business_income_q4 = []

    net_profit_q1 = []
    net_profit_q4 = []

    index = -1
    for financial_data_tuple in financial_data_tuple_list:
        index = index + 1

        if financial_data_tuple is None:
            break

        financial_data = FinancialData(financial_data_tuple)
        if financial_data is None:
            break

        if index == 0:
            target = financial_data.net_profit;
        if index == constant.SEASONS_IN_A_YEAR:
            base = financial_data.net_profit;

        if "03-31" in financial_data.date:
            main_business_income_q1.append(financial_data.main_business_income)
            net_profit_q1.append(financial_data.net_profit)
        elif "12-31" in financial_data.date:
            main_business_income_q4.append(financial_data.main_business_income)
            net_profit_q4.append(financial_data.net_profit)

        if len(main_business_income_q1) > growth_year_min and len(main_business_income_q4) > growth_year_min \
                and len(net_profit_q1) > growth_year_min and len(net_profit_q4) > growth_year_min:
            break

    if analyze_growth2(main_business_income_q1, main_business_income_q4) \
            and analyze_growth2(net_profit_q1, net_profit_q4):
        stock.operation |= constant.GROWTH_TYPE

    if base != 0:
        stock.rate = round(target / base, 2)

    return stock


def analyze_share_bonus(stock, share_bonus_tuple_list):
    total_divident = 0
    year = None
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

        if share_bonus.dividend_date is None:
            break

        strings = share_bonus.dividend_date.split("-")

        if strings is None or len(strings) == 0:
            break

        year = strings[0]

        if prev_year is not None:
            if prev_year != year:
                break

        total_divident += float(share_bonus.dividend)
        stock.set_dividend(total_divident)

        if stock.price > 0:
            stock.set_dividend_yield(round(100.0 * stock.dividend / 10 / stock.price, 2))

        prev_year = year;

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

        # if not stock.check_out():
        #     continue

        count += 1

        print(index, stock.code, stock.name, stock.mark, stock.operation)

        stock_data_tuple_list = read_stock_data_from_database(stock)
        financial_data_tuple_list = read_financial_data_from_database(stock)
        share_bonus_tuple_list = read_share_bonus_from_database(stock)

        stock = analyze_share_bonus(stock, share_bonus_tuple_list)
        stock = analyze_stock_data(stock, stock_data_tuple_list, financial_data_tuple_list)
        stock = analyze_financial_data(stock, financial_data_tuple_list)

        stock.update_to_database()

    print("analyze done, count=", count)


def select(where=None, order=None, sort=None):
    make_data_directory()

    stock_tuple_list = read_stock_tuple_list_from_database(where, order, sort)
    write_stock_to_file(stock_tuple_list)

    for stock_tuple in stock_tuple_list:
        stock = Stock(stock_tuple)

        if not stock.check_out():
            continue

        print("\"" + stock.code + "\"" + ", #" + stock.name + " "
              + "roe " + str(stock.roe) + " "
              + "pe " + str(stock.pe) + " pb " + str(stock.pb) + " "
              + "dividend " + str(stock.dividend) + " " + str(stock.dividend_yield) + "% "
              + " operation " + str(stock.operation) + " discount " + str(stock.discount))

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

    black_stock_list = black.get_stock_list()
    if black_stock_list is None:
        return

    favorite_stock_list = favorite.get_stock_list()
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

        stock.set_mark(constant.STOCK_TYPE_NONE)

        if stock.code in favorite_stock_list:
            stock.set_mark(constant.STOCK_TYPE_FAVORITE)

        if stock.code in black_stock_list:
            stock.set_mark(constant.STOCK_TYPE_BLACK)

        stock.update_to_database()
        count += 1

        print(index, stock.code, stock.name, stock.operation, stock.mark, stock.discount)

    print("update done, count=", count)


class Stock():
    def __init__(self, stock=None):
        self.id = 0
        self.classes = ""
        self.se = ""
        self.code = ""
        self.name = ""
        self.pinyin = ""
        self.mark = 0
        self.price = 0
        self.change = 0
        self.net = 0
        self.volume = 0
        self.value = 0
        self.operation = 0
        self.hold = 0
        self.cost = 0
        self.profit = 0
        self.total_share = 0
        self.roe = 0
        self.rate = 0
        self.valuation = 0
        self.discount = 0
        self.pe = 0
        self.pb = 0
        self.dividend = 0
        self.dividend_yield = 0
        self.delta = 0
        self.time_to_market = ""
        self.created = ""
        self.modified = ""

        if isinstance(stock, dict):
            se = stock["symbol"][0:2]

            self.set_se(se)
            self.set_code(stock['code'])
            self.set_name(stock['name'])
            self.set_price(stock['price'])
            self.set_change(stock['change'])
            self.set_net(stock['net'])
        elif isinstance(stock, tuple):
            self.set_id(stock[0])
            self.set_classes(stock[database_contract.StockColumn.classes.value])
            self.set_se(stock[database_contract.StockColumn.se.value])
            self.set_code(stock[database_contract.StockColumn.code.value])
            self.set_name(stock[database_contract.StockColumn.name.value])
            self.set_pinyin(stock[database_contract.StockColumn.pinyin.value])
            self.set_mark(stock[database_contract.StockColumn.mark.value])
            self.set_price(stock[database_contract.StockColumn.price.value])
            self.set_change(stock[database_contract.StockColumn.change.value])
            self.set_net(stock[database_contract.StockColumn.net.value])
            self.set_volume(stock[database_contract.StockColumn.volume.value])
            self.set_value(stock[database_contract.StockColumn.value.value])
            self.set_operation(stock[database_contract.StockColumn.operation.value])
            self.set_hold(stock[database_contract.StockColumn.hold.value])
            self.set_cost(stock[database_contract.StockColumn.cost.value])
            self.set_profit(stock[database_contract.StockColumn.profit.value])
            self.set_total_share(stock[database_contract.StockColumn.total_share.value])
            self.set_roe(stock[database_contract.StockColumn.roe.value])
            self.set_rate(stock[database_contract.StockColumn.rate.value])
            self.set_valuation(stock[database_contract.StockColumn.valuation.value])
            self.set_discount(stock[database_contract.StockColumn.discount.value])
            self.set_pe(stock[database_contract.StockColumn.pe.value])
            self.set_pb(stock[database_contract.StockColumn.pb.value])
            self.set_dividend(stock[database_contract.StockColumn.dividend.value])
            self.set_dividend_yield(stock[database_contract.StockColumn.dividend_yield.value])
            self.set_delta(stock[database_contract.StockColumn.delta.value])
            self.set_time_to_market(stock[database_contract.StockColumn.time_to_market.value])
            self.set_created(stock[database_contract.StockColumn.created.value])
            self.set_modified(stock[database_contract.StockColumn.modified.value])

    def set_id(self, id):
        if id is not None:
            self.id = id

    def set_classes(self, classes):
        if classes is not None:
            self.classes = classes

    def set_se(self, se):
        if se is not None:
            self.se = se

    def set_code(self, code):
        if code is not None:
            self.code = code

    def set_name(self, name):
        if name is not None:
            self.name = name

    def set_pinyin(self, pinyin):
        if pinyin is not None:
            self.pinyin = pinyin

    def set_mark(self, mark):
        if mark is not None:
            self.mark = mark

    def set_price(self, price):
        if price is not None:
            self.price = price

    def set_change(self, change):
        if change is not None:
            self.change = change

    def set_net(self, net):
        if net is not None:
            self.net = net

    def set_volume(self, volume):
        if volume is not None:
            self.volume = volume

    def set_value(self, value):
        if value is not None:
            self.value = value

    def set_operation(self, operation):
        if operation is not None:
            self.operation = operation

    def set_hold(self, hold):
        if hold is not None:
            self.hold = hold

    def set_cost(self, cost):
        if cost is not None:
            self.cost = cost

    def set_profit(self, profit):
        if profit is not None:
            self.profit = profit

    def set_total_share(self, total_share):
        if total_share is not None:
            self.total_share = total_share

    def set_roe(self, roe):
        if roe is not None:
            self.roe = roe

    def set_rate(self, rate):
        if rate is not None:
            self.rate = rate

    def set_valuation(self, valuation):
        if valuation is not None:
            self.valuation = valuation

    def set_discount(self, discount):
        if discount is not None:
            self.discount = discount

    def set_pe(self, pe):
        if pe is not None:
            self.pe = pe

    def set_pb(self, pb):
        if pb is not None:
            self.pb = pb

    def set_dividend(self, dividend):
        if dividend is not None:
            self.dividend = dividend

    def set_dividend_yield(self, dividend_yield):
        if dividend_yield is not None:
            self.dividend_yield = dividend_yield

    def set_delta(self, delta):
        if delta is not None:
            self.delta = delta

    def set_time_to_market(self, time_to_market):
        if time_to_market is not None:
            self.time_to_market = time_to_market

    def set_created(self, created):
        if created is not None:
            self.created = created

    def set_modified(self, modified):
        if modified is not None:
            self.modified = modified

    def get_insert_tuple(self):
        return tuple((self.se, self.code, self.name,
                      self.price, self.change, self.net,
                      self.created, self.modified))

    def get_update_tuple(self):
        return tuple((self.se, self.code, self.name,
                      self.price, self.change, self.net,
                      self.modified,
                      self.code))

    def is_favorite(self):
        result = False

        favorite_stock_list = favorite.get_stock_list()

        if favorite_stock_list is None:
            return result

        if self.code in favorite_stock_list:
            result = True

        return result

    def is_special_treatment(self):
        result = False

        if "ST" in self.name:
            result = True

        return result

    def is_time_to_market_too_short(self):
        result = False

        if self.time_to_market is None:
            return result

        if len(self.time_to_market) < len(constant.DATE_FORMAT):
            return result

        time_to_market_min = datetime.now() - relativedelta(years=constant.TIME_TO_MARKET_YEAR_MIN)
        time_to_market = datetime.strptime(self.time_to_market, constant.DATE_FORMAT)

        if time_to_market > time_to_market_min:
            result = True

        return result

    def check_out(self):
        result = False
        black_stock_list = black.get_stock_list()

        if favorite_only:
            if self.is_favorite():
                return True
            else:
                return False
        else:
            if self.is_special_treatment():
                return False
            elif self.is_time_to_market_too_short():
                return False
            elif self.code in black_stock_list:
                return False
            else:
                result = True

        return result

    def update_to_database(self):
        connect = None
        sql_update = "UPDATE stock SET" \
                     " classes=?, pinyin=?," \
                     " mark=?, operation=?," \
                     " total_share=?, roe=?, rate=?, " \
                     " valuation=?, discount=?," \
                     " pe=?, pb=?," \
                     " dividend=?, dividend_yield=?,  delta=?," \
                     " time_to_market=? WHERE code=?"
        try:
            connect = sqlite3.connect(database_contract.DATABASE_FILE_NAME)
            cursor = connect.cursor()
            cursor.execute(sql_update, (self.classes, self.pinyin,
                                        self.mark, self.operation,
                                        self.total_share, self.roe, self.rate,
                                        self.valuation, self.discount,
                                        self.pe, self.pb,
                                        self.dividend, self.dividend_yield, self.delta,
                                        self.time_to_market, self.code))
            connect.commit()
        except sqlite3.Error as e:
            print('e:', e)
        finally:
            if connect is not None:
                connect.close()

    @staticmethod
    def get_query_sql(where=None, order=None, sort=None):
        query_sql = "SELECT * FROM stock"

        if where is not None:
            query_sql += " WHERE " + where

        if order is not None:
            query_sql += " ORDER BY " + order

        if sort is not None:
            query_sql += " " + sort

        return query_sql

    @staticmethod
    def get_insert_sql():
        insert_sql = "INSERT INTO stock (" \
                     "se, code, name, " \
                     "price, change, net, " \
                     "created, modified" \
                     ") VALUES(" \
                     "?,?,?," \
                     "?,?,?," \
                     "?,?)"
        return insert_sql

    @staticmethod
    def get_update_sql():
        update_sql = "UPDATE stock SET " \
                     "se=?, code=?, name=?, " \
                     "price=?, change=?, net=?, " \
                     "modified=? " \
                     " WHERE " \
                     "code=?"
        return update_sql


class StockData:
    def __init__(self, stock_data_tuple=None):
        self.id = 0
        self.stock_code = ""
        self.date = ""
        self.time = ""
        self.period = ""
        self.open = 0
        self.high = 0
        self.low = 0
        self.close = 0
        self.volume = 0
        self.created = ""
        self.modified = ""

        if stock_data_tuple is None:
            return

        self.set_id(stock_data_tuple[0])
        self.set_stock_code(stock_data_tuple[database_contract.StockDataColumn.stock_code.value])
        self.set_date(stock_data_tuple[database_contract.StockDataColumn.date.value])
        self.set_time(stock_data_tuple[database_contract.StockDataColumn.time.value])
        self.set_period(stock_data_tuple[database_contract.StockDataColumn.period.value])
        self.set_open(stock_data_tuple[database_contract.StockDataColumn.open.value])
        self.set_high(stock_data_tuple[database_contract.StockDataColumn.high.value])
        self.set_low(stock_data_tuple[database_contract.StockDataColumn.low.value])
        self.set_close(stock_data_tuple[database_contract.StockDataColumn.close.value])
        self.set_volume(stock_data_tuple[database_contract.StockDataColumn.volume.value])
        self.set_created(stock_data_tuple[database_contract.StockDataColumn.created.value])
        self.set_modified(stock_data_tuple[database_contract.StockDataColumn.modified.value])

    def set_id(self, id):
        if id is not None:
            self.id = id

    def set_stock_code(self, stock_code):
        if stock_code is not None:
            self.stock_code = stock_code

    def set_date(self, date):
        if date is not None:
            self.date = date

    def set_time(self, time):
        if time is not None:
            self.time = time

    def set_period(self, period):
        if period is not None:
            self.period = period

    def set_open(self, open):
        if open is not None:
            self.open = open

    def set_high(self, high):
        if high is not None:
            self.high = high

    def set_low(self, low):
        if low is not None:
            self.low = low

    def set_close(self, close):
        if close is not None:
            self.close = close

    def set_volume(self, volume):
        if volume is not None:
            self.volume = volume

    def set_created(self, created):
        if created is not None:
            self.created = created

    def set_modified(self, modified):
        if modified is not None:
            self.modified = modified


class FinancialData:
    def __init__(self, financial_data_tuple=None):
        self.id = 0
        self.stock_code = ""
        self.date = ""
        self.book_value_per_share = 0
        self.cash_flow_per_share = 0
        self.total_current_assets = 0
        self.total_assets = 0
        self.total_long_term_liabilities = 0
        self.main_business_income = 0
        self.financial_expenses = 0
        self.net_profit = 0
        self.net_profit_per_share = 0
        self.created = ""
        self.modified = ""

        if financial_data_tuple is None:
            return

        self.set_id(financial_data_tuple[0])
        self.set_stock_code(financial_data_tuple[database_contract.FinancialDataColumn.stock_code.value])
        self.set_date(financial_data_tuple[database_contract.FinancialDataColumn.date.value])
        self.set_book_value_per_share(financial_data_tuple[database_contract.FinancialDataColumn.book_value_per_share.value])
        self.set_cash_flow_per_share(financial_data_tuple[database_contract.FinancialDataColumn.cash_flow_per_share.value])
        self.set_total_current_assets(financial_data_tuple[database_contract.FinancialDataColumn.total_current_assets.value])
        self.set_total_assets(financial_data_tuple[database_contract.FinancialDataColumn.total_assets.value])
        self.set_total_long_term_liabilities(financial_data_tuple[database_contract.FinancialDataColumn.total_long_term_liabilities.value])
        self.set_main_business_income(financial_data_tuple[database_contract.FinancialDataColumn.main_business_income.value])
        self.set_financial_expenses(financial_data_tuple[database_contract.FinancialDataColumn.financial_expenses.value])
        self.set_net_profit(financial_data_tuple[database_contract.FinancialDataColumn.net_profit.value])
        self.set_net_profit_per_share(financial_data_tuple[database_contract.FinancialDataColumn.net_profit_per_share.value])
        self.set_created(financial_data_tuple[database_contract.FinancialDataColumn.created.value])
        self.set_modified(financial_data_tuple[database_contract.FinancialDataColumn.modified.value])

    def set_id(self, id):
        if id is not None:
            self.id = id

    def set_stock_code(self, stock_code):
        if stock_code is not None:
            self.stock_code = stock_code

    def set_date(self, date):
        if date is not None:
            self.date = date

    def set_book_value_per_share(self, book_value_per_share):
        if book_value_per_share is not None:
            self.book_value_per_share = book_value_per_share

    def set_cash_flow_per_share(self, cash_flow_per_share):
        if cash_flow_per_share is not None:
            self.cash_flow_per_share = cash_flow_per_share

    def set_total_current_assets(self, total_current_assets):
        if total_current_assets is not None:
            self.total_current_assets = total_current_assets

    def set_total_assets(self, total_assets):
        if total_assets is not None:
            self.total_assets = total_assets

    def set_total_long_term_liabilities(self, total_long_term_liabilities):
        if total_long_term_liabilities is not None:
            self.total_long_term_liabilities = total_long_term_liabilities

    def set_main_business_income(self, main_business_income):
        if main_business_income is not None:
            self.main_business_income = main_business_income

    def set_financial_expenses(self, financial_expenses):
        if financial_expenses is not None:
            self.financial_expenses = financial_expenses

    def set_net_profit(self, net_profit):
        if net_profit is not None:
            self.net_profit = net_profit

    def set_net_profit_per_share(self, net_profit_per_share):
        if net_profit_per_share is not None:
            self.net_profit_per_share = net_profit_per_share

    def set_created(self, created):
        if created is not None:
            self.created = created

    def set_modified(self, modified):
        if modified is not None:
            self.modified = modified


class ShareBonus:
    def __init__(self, share_bonus_tuple=None):
        self.id = 0
        self.stock_code = ""
        self.date = ""
        self.dividend = ""
        self.dividend_date = ""
        self.created = ""
        self.modified = ""

        if share_bonus_tuple is None:
            return

        self.set_id(share_bonus_tuple[0])
        self.set_stock_code(share_bonus_tuple[database_contract.ShareBonusColumn.stock_code.value])
        self.set_date(share_bonus_tuple[database_contract.ShareBonusColumn.date.value])
        self.set_dividend(share_bonus_tuple[database_contract.ShareBonusColumn.dividend.value])
        self.set_dividend_date(share_bonus_tuple[database_contract.ShareBonusColumn.dividend_date.value])
        self.set_created(share_bonus_tuple[database_contract.ShareBonusColumn.created.value])
        self.set_modified(share_bonus_tuple[database_contract.ShareBonusColumn.modified.value])


    def set_id(self, id):
        if id is not None:
            self.id = id

    def set_stock_code(self, stock_code):
        if stock_code is not None:
            self.stock_code = stock_code

    def set_date(self, date):
        if date is not None:
            self.date = date

    def set_dividend(self, dividend):
        if dividend is not None:
            self.dividend = dividend

    def set_dividend_date(self, dividend_date):
        if dividend_date is not None:
            self.dividend_date = dividend_date

    def set_created(self, created):
        if created is not None:
            self.created = created

    def set_modified(self, modified):
        if modified is not None:
            self.modified = modified
