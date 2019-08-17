# -*- coding: utf-8 -*-
import pandas
from dateutil.relativedelta import relativedelta

import constant
import csv
import os
import sina_financial
import sqlite3
import tushare

import favorite

from datetime import datetime

favorite_only = False


def setup_database():
    connect = None

    print("setup_database")

    try:
        connect = sqlite3.connect(constant.DATABASE_NAME)
        if connect is not None:
            cursor = connect.cursor()
            cursor.execute(constant.SQL_SETUP_TABLE_STOCK)
            cursor.execute(constant.SQL_SETUP_TABLE_STOCK_DATA)
            cursor.execute(constant.SQL_SETUP_TABLE_FINANCIAL_DATA)
            cursor.execute(constant.SQL_SETUP_TABLE_SHARE_BONUS)
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


def get_stock_basics_from_tushare():
    stock_basics = tushare.get_stock_basics()
    if stock_basics is None:
        print("stock_basics is None, return None")
        return None

    stock_basics.reset_index(level=0, inplace=True)
    stock_basics = stock_basics.sort_values(by='code').reset_index(drop=True)

    return stock_basics


def get_not_before(stock_data_list):
    not_before = None

    if stock_data_list is None:
        return not_before

    if stock_data_list is not None:
        not_before = stock_data_list[0]["date"]

    return not_before


def download():
    not_before = None

    download_stock_basic()

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

        if not stock.check_out():
            continue

        count += 1

        print(index, stock.code, stock.name, stock.rating, stock.favorite)

        stock_data_list = download_stock_data(stock)

        not_before = get_not_before(stock_data_list)

        financial_data_list = download_financial_data(stock, not_before)

        download_share_bonus(stock)

    print("download done, count=", count)


def download_stock_basic():
    stock_basics = get_stock_basics_from_tushare()
    write_stock_basics_to_database(stock_basics)


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


def download_financial_data(stock, not_before=None):
    time_to_market_len_min = constant.TIME_TO_MARKET_YEAR_MIN * constant.SEASONS_IN_A_YEAR

    # book_value_per_share = {}
    # earnings_per_share = {}
    # cash_flow_per_share = {}
    # total_current_assets = {}
    # total_assets = {}
    # total_long_term_liabilities = {}
    # main_business_income = {}
    # financial_expenses = {}
    # net_profit = {}

    financial_data_list = []
    test_financial_data_list = []

    if stock is None:
        return None

    if not_before is not None:
        not_before = datetime.strptime(not_before, constant.DATE_FORMAT)

    sina = sina_financial.SinaFinancial()

    # print("download_financial_data code=", stock.code)

    # book_value_per_share = sina.download_financial_data(stock.code, 'mgjzc')
    # earnings_per_share = sina.download_financial_data(stock.code, 'mgsy')
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
    #     financial_data["earnings_per_share"] = get_value_string_by_key(key, earnings_per_share)
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

    financial_data_list = sina.download_financial_data(stock.code, not_before)

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
    return financial_data_list


def download_share_bonus(stock):
    if stock is None:
        return None

    sina = sina_financial.SinaFinancial()

    share_bonus_list = sina.download_share_bonus(stock.code)

    write_share_bonus_to_database(stock.code, share_bonus_list)

    return share_bonus_list


def write_stock_basics_to_database(stock_basics):
    connect = None
    executemany = False
    favorite_stock = 0
    insert_tuple_list = []

    sql_query = Stock.get_sql_query()
    sql_insert = "INSERT INTO stock (" \
                 "code, name, industry, area, pe," \
                 "outstanding, totals, total_assets, liquid_assets, fixed_assets," \
                 "reserved, rps, eps, bvps, pb," \
                 "time_to_market, undp, perundp, rev, profit," \
                 "gpr, npr, holders, dividend_yield, dividend," \
                 "rating, favorite, created, modified" \
                 ") VALUES(" \
                 "?,?,?,?,?," \
                 "?,?,?,?,?," \
                 "?,?,?,?,?," \
                 "?,?,?,?,?," \
                 "?,?,?,?,?," \
                 "?,?,?,?)"
    sql_update = "UPDATE stock SET " \
                 "name=?, industry=?, area=?, pe=?," \
                 "outstanding=?, totals=?, total_assets=?, liquid_assets=?, fixed_assets=?," \
                 "reserved=?, rps=?, eps=?, bvps=?, pb=?," \
                 "time_to_market=?, undp=?, perundp=?, rev=?, profit=?," \
                 "gpr=?, npr=?, holders=?, dividend_yield=?, dividend=?," \
                 "rating=?, favorite=?, modified=?" \
                 " WHERE " \
                 "id=?"

    print("write_stock_basics_to_database")

    if stock_basics is None:
        print("stock_basics is None, return")
        return

    stock_favorite_list = favorite.get_stock_favorite_list()

    setup_database()

    try:
        connect = sqlite3.connect(constant.DATABASE_NAME)
        cursor = connect.cursor()

        cursor.execute(sql_query)
        if cursor.fetchone() is None:
            executemany = True

        stock_basic_list = stock_basics.to_dict('records')
        for stock_basic in stock_basic_list:
            stock = Stock()
            stock.set_stock_basic(stock_basic)

            if stock_favorite_list is not None:
                favorite_stock = 0
                if stock.code in stock_favorite_list:
                    favorite_stock = 1

            now = datetime.now().strftime(constant.DATE_TIME_FORMAT)

            if executemany:
                stock.set_favorite(favorite_stock)
                stock.set_created(now)
                stock.set_modified(now)

                insert_tuple = stock.get_insert_tuple()
                insert_tuple_list.append(insert_tuple)
            else:
                sql_check_record_exist = "SELECT * FROM stock WHERE code=?"
                cursor.execute(sql_check_record_exist, (stock.code,))
                stock_tuple = cursor.fetchone()
                if stock_tuple is None:
                    stock.set_favorite(favorite_stock)
                    stock.set_created(now)
                    stock.set_modified(now)

                    insert_tuple = stock.get_insert_tuple()

                    cursor.execute(sql_insert, insert_tuple)
                    connect.commit()
                    print("insert stock:", insert_tuple)
                else:
                    stock.set_favorite(favorite_stock)
                    stock.set_modified(now)
                    update_tuple = stock.get_update_tuple()
                    cursor.execute(sql_update, update_tuple)
                    connect.commit()
                    print("update stock:", update_tuple)
        if executemany:
            print("insert: executemany")
            cursor.executemany(sql_insert, insert_tuple_list)
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
        connect = sqlite3.connect(constant.DATABASE_NAME)
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
    sql_insert = "INSERT INTO financial_data (stock_code, date, " \
                 "book_value_per_share, earnings_per_share, cash_flow_per_share, " \
                 "total_current_assets, total_assets, total_long_term_liabilities, " \
                 "main_business_income, financial_expenses, net_profit, roe, book_value_per_share_rate, " \
                 "created, modified)" \
                 " VALUES(?,?," \
                 "?,?,?," \
                 "?,?,?," \
                 "?,?,?,?,?," \
                 "?,?)"

    if financial_data_list is None:
        print("financial_data_list is None, return")
        return

    try:
        connect = sqlite3.connect(constant.DATABASE_NAME)
        cursor = connect.cursor()

        cursor.execute(sql_delete, (code,))

        index = -1
        for financial_data in financial_data_list:
            index = index + 1

            date = financial_data['date']
            book_value_per_share = financial_data['book_value_per_share']
            earnings_per_share = financial_data['earnings_per_share']
            cash_flow_per_share = financial_data['cash_flow_per_share']
            total_current_assets = financial_data['total_current_assets']
            total_assets = financial_data['total_assets']
            total_long_term_liabilities = financial_data['total_long_term_liabilities']
            main_business_income = financial_data['main_business_income']
            financial_expenses = financial_data['financial_expenses']
            net_profit = financial_data['net_profit']
            roe = financial_data['roe']
            book_value_per_share_rate = financial_data['book_value_per_share_rate']

            now = datetime.now().strftime(constant.DATE_TIME_FORMAT)

            record = tuple((code, date, book_value_per_share, earnings_per_share, cash_flow_per_share,
                            total_current_assets, total_assets, total_long_term_liabilities,
                            main_business_income, financial_expenses, net_profit, roe, book_value_per_share_rate,
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
        connect = sqlite3.connect(constant.DATABASE_NAME)
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

    field_name_tuple = tuple(("id", "code", "name",
                              "industry", "area",
                              "time_to_market", "holders",
                              "favorite", "pe", "pb", "roe",
                              "created", "modified"))

    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name_tuple)
        writer.writeheader()

        for stock_tuple in stock_tuple_list:
            stock = Stock(stock_tuple)
            if stock is None:
                continue

            stock_dict = {"id": stock.id, "code": stock.code, "name": stock.name,
                          "industry": stock.industry, "area": stock.area,
                          "time_to_market": stock.time_to_market, "holders": stock.holders,
                          "favorite": stock.favorite, "pe": stock.pe, "pb": stock.pb,
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
                              "earnings_per_share",
                              "cash_flow_per_share",
                              "total_current_assets",
                              "total_assets",
                              "total_long_term_liabilities",
                              "main_business_income",
                              "financial_expenses",
                              "net_profit",
                              "roe",
                              "book_value_per_share_rate"))

    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name_tuple)
        writer.writeheader()

        for financial_data_tuple in financial_data_tuple_list:
            financial_data = FinancialData(financial_data_tuple)
            if financial_data is None:
                continue

            financial_data_dict = {"date": financial_data.date,
                               "book_value_per_share": financial_data.book_value_per_share,
                               "earnings_per_share": financial_data.earnings_per_share,
                               "cash_flow_per_share": financial_data.cash_flow_per_share,
                               "total_current_assets": financial_data.total_current_assets,
                               "total_assets": financial_data.total_assets,
                               "total_long_term_liabilities": financial_data.total_long_term_liabilities,
                               "main_business_income": financial_data.main_business_income,
                               "financial_expenses": financial_data.financial_expenses,
                               "net_profit": financial_data.net_profit,
                               "roe": financial_data.roe,
                               "book_value_per_share_rate": financial_data.book_value_per_share_rate,
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
#         connect = sqlite3.connect(constant.DATABASE_NAME)
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

    sql_query = Stock.get_sql_query(where, order, sort)

    try:
        connect = sqlite3.connect(constant.DATABASE_NAME)
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
        connect = sqlite3.connect(constant.DATABASE_NAME)
        cursor = connect.cursor()
        cursor.execute(sql_query, (stock.code, period))
        stock_data_tuple_list = cursor.fetchall()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()

    return stock_data_tuple_list


def analyze_stock_data(stock, stock_data_tuple_list, financial_data_tuple_list, share_bonus_tuple_list):
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

    if share_bonus_tuple_list is None:
        return stock

    if len(share_bonus_tuple_list) < 1:
        return stock

    stock_data_tuple = stock_data_tuple_list[0]
    financial_data_tuple = financial_data_tuple_list[0]
    share_bonus_tuple = share_bonus_tuple_list[0]

    stock_data = StockData(stock_data_tuple)
    if stock_data is None:
        return stock

    financial_data = FinancialData(financial_data_tuple)
    if financial_data is None:
        return stock

    share_bonus = ShareBonus(share_bonus_tuple)
    if share_bonus is None:
        return stock

    if stock_data.close > 0:
        stock.dividend_yield = 100.0 * share_bonus.dividend / 10 / stock_data.close
        stock.dividend = share_bonus.dividend

    # if financial_data.earnings_per_share != 0:
    #     stock.pe = stock_data.close / financial_data.earnings_per_share
    #
    # if financial_data.book_value_per_share != 0:
    #     stock.pb = stock_data.close / financial_data.book_value_per_share

    if (0 < stock.pe < constant.PE_MAX) and (0 < stock.pb < constant.PB_MAX):
        stock.rating |= constant.PRICE_TYPE

    if financial_data.total_long_term_liabilities < financial_data.main_business_income:
        stock.rating |= constant.LIABILITIES_TYPE

    return stock


def read_financial_data_from_database(stock):
    connect = None
    financial_data_tuple_list = tuple()
    sql_query = "SELECT * FROM financial_data WHERE stock_code = ?  order by date desc"
    if stock is None:
        return None

    try:
        connect = sqlite3.connect(constant.DATABASE_NAME)
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
        connect = sqlite3.connect(constant.DATABASE_NAME)
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

        # if index == 0:
        #     if not financial_data.check_out():
        #         stock.rating = constant.POOR_TYPE
        #         print("stock.rating = constant.POOR_TYPE")
        #         return stock

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
        stock.rating |= constant.GROWTH_TYPE

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

        if not stock.check_out():
            continue

        count += 1

        print(index, stock.code, stock.name, stock.rating, stock.favorite)

        stock_data_tuple_list = read_stock_data_from_database(stock)
        financial_data_tuple_list = read_financial_data_from_database(stock)
        share_bonus_tuple_list = read_share_bonus_from_database(stock)

        stock = analyze_stock_data(stock, stock_data_tuple_list, financial_data_tuple_list, share_bonus_tuple_list)
        stock = analyze_financial_data(stock, financial_data_tuple_list)
        stock.update_to_database()

    print("analyze done, count=", count)


def select(where=None, order=None, sort=None):
    make_data_directory()

    stock_tuple_list = read_stock_tuple_list_from_database(where, order, sort)
    write_stock_to_file(stock_tuple_list)

    print("select done, count=", len(stock_tuple_list))

    return stock_tuple_list


def write_to_file(stock):
    if stock is None:
        return

    print(stock.code, stock.name, round(stock.dividend_yield, 2), round(stock.dividend, 2), " ", stock.rating,
          stock.favorite)

    stock_data_tuple_list = read_stock_data_from_database(stock)
    write_stock_data_to_file(stock, stock_data_tuple_list)

    financial_data_tuple_list = read_financial_data_from_database(stock)
    write_financial_data_to_file(stock, financial_data_tuple_list)

    share_bonus_tuple_list = read_share_bonus_from_database(stock)
    write_share_bonus_to_file(stock, share_bonus_tuple_list)


class StockBasic:
    def __init__(self, stock_basic=None):
        if stock_basic is None:
            return

        self.set(stock_basic)

        # self.code = stock_basic['code'] # code, 代码
        # self.name = stock_basic['name']  # name, 名称
        # self.industry = stock_basic['industry']  # industry, 所属行业
        # self.area = stock_basic['area']  # area, 地区
        # self.pe = stock_basic['pe']  # pe, 市盈率
        # self.outstanding = stock_basic['outstanding']  # outstanding, 流通股本(亿)
        # self.totals = stock_basic['totals']  # totals, 总股本(亿)
        # self.total_assets = stock_basic['totalAssets']  # totalAssets, 总资产(万)
        # self.liquid_assets = stock_basic['liquidAssets']  # liquidAssets, 流动资产
        # self.fixed_assets = stock_basic['fixedAssets']  # fixedAssets, 固定资产
        # self.reserved = stock_basic['reserved']  # reserved, 公积金
        # self.rps = stock_basic['reservedPerShare']  # reservedPerShare, 每股公积金
        # self.eps = stock_basic['esp']  # esp, 每股收益
        # self.bvps = stock_basic['bvps']  # bvps, 每股净资
        # self.pb = stock_basic['pb']  # pb, 市净率
        # self.time_to_market = str(stock_basic['timeToMarket'])  # timeToMarket, 上市日期
        # self.undp = stock_basic['undp']  # undp, 未分利润
        # self.perundp = stock_basic['perundp']  # perundp, 每股未分配
        # self.rev = stock_basic['rev']  # rev, 收入同比( %)
        # self.profit = stock_basic['profit']  # profit, 利润同比( %)
        # self.gpr = stock_basic['gpr']  # gpr, 毛利率( %)
        # self.npr = stock_basic['npr']  # npr, 净利润率( %)
        # self.holders = stock_basic['holders']  # holders, 股东人数

    def set_code(self, code):
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_industry(self, industry):
        self.industry = industry

    def set_area(self, area):
        self.area = area

    def set_pe(self, pe):
        self.pe = pe

    def set_outstanding(self, outstanding):
        self.outstanding = outstanding

    def set_totals(self, totals):
        self.totals = totals

    def set_total_assets(self, total_assets):
        self.total_assets = total_assets

    def set_liquid_assets(self, liquid_assets):
        self.liquid_assets = liquid_assets

    def set_fixed_assets(self, fixed_assets):
        self.fixed_assets = fixed_assets

    def set_reserved(self, reserved):
        self.reserved = reserved

    def set_rps(self, rps):
        self.rps = rps

    def set_eps(self, eps):
        self.eps = eps

    def set_bvps(self, bvps):
        self.bvps = bvps

    def set_pb(self, pb):
        self.pb = pb

    def set_time_to_market(self, time_to_market):
        time_to_market = str(time_to_market)

        if len(time_to_market) == 8:
            time_to_market = time_to_market[:4] + "-" + time_to_market[4:6] + "-" + time_to_market[6:]

        self.time_to_market = time_to_market

    def set_undp(self, undp):
        self.undp = undp

    def set_perundp(self, perundp):
        self.perundp = perundp

    def set_rev(self, rev):
        self.rev = rev

    def set_profit(self, profit):
        self.profit = profit

    def set_gpr(self, gpr):
        self.gpr = gpr

    def set_npr(self, npr):
        self.npr = npr

    def set_holders(self, holders):
        self.holders = holders

    def set(self, stock_basic):
        if stock_basic is None:
            return
        if isinstance(stock_basic, dict):
            self.set_code(stock_basic['code'])
            self.set_name(stock_basic['name'])
            self.set_industry(stock_basic['industry'])  # industry, 所属行业
            self.set_area(stock_basic['area'])  # area, 地区
            self.set_pe(stock_basic['pe'])  # pe, 市盈率
            self.set_outstanding(stock_basic['outstanding'])  # outstanding, 流通股本(亿)
            self.set_totals(stock_basic['totals'])  # totals, 总股本(亿)
            self.set_total_assets(stock_basic['totalAssets'])  # totalAssets, 总资产(万)
            self.set_liquid_assets(stock_basic['liquidAssets'])  # liquidAssets, 流动资产
            self.set_fixed_assets(stock_basic['fixedAssets'])  # fixedAssets, 固定资产
            self.set_reserved(stock_basic['reserved'])  # reserved, 公积金
            self.set_rps(stock_basic['reservedPerShare'])  # reservedPerShare, 每股公积金
            self.set_eps(stock_basic['esp'])  # esp, 每股收益
            self.set_bvps(stock_basic['bvps'])  # bvps, 每股净资
            self.set_pb(stock_basic['pb'])  # pb, 市净率
            self.set_time_to_market(stock_basic['timeToMarket'])  # timeToMarket, 上市日期
            self.set_undp(stock_basic['undp'])  # undp, 未分利润
            self.set_perundp(stock_basic['perundp'])  # perundp, 每股未分配
            self.set_rev(stock_basic['rev'])  # rev, 收入同比( %)
            self.set_profit(stock_basic['profit'])  # profit, 利润同比( %)
            self.set_gpr(stock_basic['gpr'])  # gpr, 毛利率( %)
            self.set_npr(stock_basic['npr'])  # npr, 净利润率( %)
            self.set_holders(stock_basic['holders'])  # holders, 股东人数
        else:
            self.set_code(stock_basic[1])
            self.set_name(stock_basic[2])
            self.set_industry(stock_basic[3])  # industry, 所属行业
            self.set_area(stock_basic[4])  # area, 地区
            self.set_pe(stock_basic[5])  # pe, 市盈率
            self.set_outstanding(stock_basic[6])  # outstanding, 流通股本(亿)
            self.set_totals(stock_basic[7])  # totals, 总股本(亿)
            self.set_total_assets(stock_basic[8])  # totalAssets, 总资产(万)
            self.set_liquid_assets(stock_basic[9])  # liquidAssets, 流动资产
            self.set_fixed_assets(stock_basic[10])  # fixedAssets, 固定资产
            self.set_reserved(stock_basic[11])  # reserved, 公积金
            self.set_rps(stock_basic[12])  # reservedPerShare, 每股公积金
            self.set_eps(stock_basic[13])  # esp, 每股收益
            self.set_bvps(stock_basic[14])  # bvps, 每股净资
            self.set_pb(stock_basic[15])  # pb, 市净率
            self.set_time_to_market(stock_basic[16])  # timeToMarket, 上市日期
            self.set_undp(stock_basic[17])  # undp, 未分利润
            self.set_perundp(stock_basic[18])  # perundp, 每股未分配
            self.set_rev(stock_basic[19])  # rev, 收入同比( %)
            self.set_profit(stock_basic[20])  # profit, 利润同比( %)
            self.set_gpr(stock_basic[21])  # gpr, 毛利率( %)
            self.set_npr(stock_basic[22])  # npr, 净利润率( %)
            self.set_holders(stock_basic[23])  # holders, 股东人数


class Stock(StockBasic):
    def __init__(self, stock_tuple=None):
        if stock_tuple is None:
            self.id = 0
            self.dividend_yield = 0
            self.dividend = 0
            self.rating = 0
            self.favorite = 0
            self.created = 0
            self.modified = 0
        else:
            self.id = stock_tuple[0]
            super().__init__(stock_tuple)
            self.dividend_yield = stock_tuple[24]
            self.dividend = stock_tuple[25]
            self.rating = stock_tuple[26]
            self.favorite = stock_tuple[27]
            self.created = stock_tuple[28]
            self.modified = stock_tuple[29]

    def set_dividend_yield(self, dividend_yield):
        self.dividend_yield = dividend_yield

    def set_dividend(self, dividend):
        self.dividend = dividend

    def set_rating(self, rating):
        self.rating = rating

    def set_favorite(self, favorite):
        self.favorite = favorite

    def set_created(self, created):
        self.created = created

    def set_modified(self, modified):
        self.modified = modified

    def set_stock_basic(self, stock_basic):
        super().set(stock_basic)

    def get_insert_tuple(self):
        return tuple((self.code, self.name, self.industry, self.area, self.pe,
                      self.outstanding, self.totals, self.total_assets, self.liquid_assets, self.fixed_assets,
                      self.reserved, self.rps, self.eps, self.bvps, self.pb,
                      self.time_to_market, self.undp, self.perundp, self.rev, self.profit,
                      self.gpr, self.npr, self.holders, self.dividend_yield, self.dividend,
                      self.rating, self.favorite, self.created, self.modified))

    def get_update_tuple(self):
        return tuple((self.name, self.industry, self.area, self.pe,
                      self.outstanding, self.totals, self.total_assets, self.liquid_assets, self.fixed_assets,
                      self.reserved, self.rps, self.eps, self.bvps, self.pb,
                      self.time_to_market, self.undp, self.perundp, self.rev, self.profit,
                      self.gpr, self.npr, self.holders, self.dividend_yield, self.dividend,
                      self.rating, self.favorite, self.modified, self.id))

    def dump(self):
        print(self.id, self.code, self.name,
              self.industry, self.area, self.time_to_market, self.holders,
              self.dividend_yield, self.dividend, self.rating, self.favorite, self.pe, self.pb,
              self.created, self.modified)

    def is_favorite(self):
        result = False

        stock_favorite_list = favorite.get_stock_favorite_list()

        if stock_favorite_list is None:
            return result

        if self.code in stock_favorite_list:
            self.set_favorite(1)
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
            # elif self.rating < 1:
            #     return False
            else:
                result = True

        return result

    def update_to_database(self):
        connect = None
        sql_update = "UPDATE stock SET dividend_yield=?, dividend=?, rating=?, favorite=? WHERE code=?"

        print("update_to_database",
              " code:", self.code,
              " name:", self.name,
              " dividend_yield=", self.dividend_yield,
              " dividend=", self.dividend,
              " rating=", self.rating,
              " favorite=", self.favorite)

        try:
            connect = sqlite3.connect(constant.DATABASE_NAME)
            cursor = connect.cursor()
            cursor.execute(sql_update, (self.dividend_yield, self.dividend, self.rating, self.favorite, self.code))
            connect.commit()
        except sqlite3.Error as e:
            print('e:', e)
        finally:
            if connect is not None:
                connect.close()

    @staticmethod
    def get_sql_query(where=None, order=None, sort=None):
        sql_query = "SELECT * FROM stock"

        if where is not None:
            sql_query += " WHERE " + where

        if order is not None:
            sql_query += " ORDER BY " + order

        if sort is not None:
            sql_query += " " + sort

        return sql_query


class StockData:
    def __init__(self, stock_data_tuple=None):
        if stock_data_tuple is None:
            return

        self.id = stock_data_tuple[0]
        self.stock_code = stock_data_tuple[1]
        self.date = stock_data_tuple[2]
        self.time = stock_data_tuple[3]
        self.period = stock_data_tuple[4]
        self.open = stock_data_tuple[5]
        self.high = stock_data_tuple[6]
        self.low = stock_data_tuple[7]
        self.close = stock_data_tuple[8]
        self.volume = stock_data_tuple[9]
        self.created = stock_data_tuple[10]
        self.modified = stock_data_tuple[11]


class FinancialData:
    def __init__(self, financial_data_tuple=None):
        if financial_data_tuple is None:
            return

        self.id = financial_data_tuple[0]
        self.stock_code = financial_data_tuple[1]
        self.date = financial_data_tuple[2]
        self.book_value_per_share = financial_data_tuple[3]
        self.earnings_per_share = financial_data_tuple[4]
        self.cash_flow_per_share = financial_data_tuple[5]
        self.total_current_assets = financial_data_tuple[6]
        self.total_assets = financial_data_tuple[7]
        self.total_long_term_liabilities = financial_data_tuple[8]
        self.main_business_income = financial_data_tuple[9]
        self.financial_expenses = financial_data_tuple[10]
        self.net_profit = financial_data_tuple[11]
        self.roe = financial_data_tuple[12]
        self.book_value_per_share_rate = financial_data_tuple[13]
        self.created = financial_data_tuple[14]
        self.modified = financial_data_tuple[15]

    def check_out(self):
        result = False

        if self.book_value_per_share < 1 \
                or self.earnings_per_share < 0 \
                or self.cash_flow_per_share < 0 \
                or self.main_business_income < 0 \
                or self.net_profit < 0 \
                or self.main_business_income < self.total_long_term_liabilities:
            result = True

        return result


class ShareBonus:
    def __init__(self, share_bonus_tuple=None):
        if share_bonus_tuple is None:
            return

        self.id = share_bonus_tuple[0]
        self.stock_code = share_bonus_tuple[1]
        self.date = share_bonus_tuple[2]
        self.dividend = share_bonus_tuple[3]
        self.dividend_date = share_bonus_tuple[4]
        self.created = share_bonus_tuple[5]
        self.modified = share_bonus_tuple[6]