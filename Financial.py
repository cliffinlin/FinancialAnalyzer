# -*- coding: utf-8 -*-
import csv
import random
import sqlite3
import time
import xml.etree.ElementTree as ET
from configparser import ConfigParser
from datetime import datetime

import pandas

import Favorite
import PrivateOwner
import Constants
import EastMoney
import StockPool
import SinaFinancial
import Utility
from FinancialData import FinancialData
from Setting import Setting
from ShareBonus import ShareBonus
from Stock import Stock
from StockData import StockData
from ShareHolder import ShareHolder
from TotalShare import TotalShare

favorite_only = True
exclude_private_owner = True
stock_pool_only = True


# TODO stock_data_list
def get_time_to_market(stock_data_list):
    time_to_market = None

    if Utility.is_empty(stock_data_list):
        return time_to_market

    time_to_market = stock_data_list[0]["date"]

    return time_to_market


def need_download_stock_list():
    setting_list = Setting.read_setting_from_database("download_stock_list")
    if Utility.is_empty(setting_list):
        return True
    else:
        setting = Setting(setting_list[0])
        if setting is None:
            return True
        else:
            return False


def download():
    print(download.__name__)

    if need_download_stock_list():
        download_stock_list()
        Setting.write_setting_to_database("download_stock_list", "")

    stock_tuple_list = read_stock_tuple_list_from_database()
    if Utility.is_empty(stock_tuple_list):
        print("stock_tuple_list is empty, return")
        return

    index = Utility.read_download_index_from_config_ini()

    i = 0
    for stock_tuple in stock_tuple_list:
        i += 1
        if i < index:
            continue

        Utility.write_download_index_to_config_ini(i)

        stock = Stock(stock_tuple)
        if stock is None:
            continue

        if not check_out(stock):
            continue

        print(i, stock.get_code(), stock.get_name())

        stock_data_list = download_stock_data(stock)

        time_to_market = get_time_to_market(stock_data_list)
        stock.set_time_to_market(time_to_market)

        download_information_data(stock)
        download_financial_data(stock)
        download_share_bonus(stock)
        download_total_share(stock)
        download_share_holder(stock)

        stock.update_to_database()

    Utility.write_download_index_to_config_ini(0)

    print("download done")


def download_stock_list():
    page = 1
    stock_list = list()

    while page:
        result = SinaFinancial.download_stock_list(page)
        if Utility.is_empty(result):
            break

        stock_list += result
        page += 1
        time.sleep(random.random())

    write_stock_list_to_database(stock_list)


def download_stock_data(stock):
    # stock_data_day_list = []
    # stock_data_week_list = []
    stock_data_month_list = []

    if stock is None:
        return None

    # stock_data_day_list = sina.download_stock_data(stock, -1, DAY)
    # write_stock_data_to_database(DAY, stock.get_code(), stock_data_day_list)
    #
    # stock_data_week_list = sina.download_stock_data(stock, -1, WEEK)
    # write_stock_data_to_database(WEEK, stock.get_code(), stock_data_week_list)

    stock_data_month_list = SinaFinancial.download_stock_data(stock, -1)
    write_stock_data_to_database(stock.get_code(), stock_data_month_list)

    return stock_data_month_list


def download_information_data(stock):
    if stock is None:
        return None

    information_data_list = SinaFinancial.download_stock_information(stock)

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

    financial_data_list = SinaFinancial.download_financial_data(stock)

    write_financial_data_to_database(stock.get_code(), financial_data_list)

    return financial_data_list


def download_share_bonus(stock):
    if stock is None:
        return None

    share_bonus_list = SinaFinancial.download_share_bonus(stock)

    write_share_bonus_to_database(stock.get_code(), share_bonus_list)

    return share_bonus_list


def download_total_share(stock):
    if stock is None:
        return None

    total_share_list = SinaFinancial.download_total_share(stock)

    write_total_share_to_database(stock.get_code(), total_share_list)

    return total_share_list


def download_share_holder(stock):
    share_holder_list_list = []

    if stock is None:
        return None

    report_date_list = EastMoney.download_report_date_list(stock)
    if Utility.is_empty(report_date_list):
        return None

    for report_date in report_date_list:
        print(report_date)

        share_holder_list = EastMoney.download_share_holder_list(stock, report_date)
        if share_holder_list is None:
            continue

        share_holder_list_list.append(share_holder_list)

    write_share_holder_to_database(stock.get_code(), share_holder_list_list)

    return share_holder_list_list


def write_stock_list_to_database(stock_list):
    connect = None
    executemany = False
    insert_tuple_list = []
    update_tuple_list = []

    query_sql = Stock.get_query_sql()
    insert_sql = Stock.get_insert_sql()
    update_sql = Stock.get_update_sql()

    if Utility.is_empty(stock_list):
        print("stock_list is empty, return")
        return

    try:
        connect = sqlite3.connect(Constants.DATA_DATABASE_ORION_DB)
        if connect is None:
            return

        cursor = connect.cursor()
        cursor.execute(query_sql)
        if Utility.is_empty(cursor.fetchone()):
            executemany = True

        for stock_dict in stock_list:
            stock = Stock(stock_dict)
            now = datetime.now().strftime(Constants.DATE_TIME_FORMAT)

            if executemany:
                stock.set_created(now)
                stock.set_modified(now)
                insert_tuple = stock.get_insert_tuple()
                insert_tuple_list.append(insert_tuple)
            else:
                sql_check_record_exist = Stock.get_query_sql(where="code=?")
                cursor.execute(sql_check_record_exist, (stock.get_code(),))
                if Utility.is_empty(cursor.fetchone()):
                    stock.set_created(now)
                    stock.set_modified(now)
                    insert_tuple = stock.get_insert_tuple()
                    insert_tuple_list.append(insert_tuple)
                else:
                    stock.set_modified(now)
                    update_tuple = stock.get_update_tuple()
                    update_tuple_list.append(update_tuple)
        if not Utility.is_empty(insert_tuple_list):
            cursor.executemany(insert_sql, insert_tuple_list)
            connect.commit()
        if not Utility.is_empty(update_tuple_list):
            cursor.executemany(update_sql, update_tuple_list)
            connect.commit()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()


def write_stock_data_to_database(stock_code, stock_data_list, period=Constants.MONTH):
    connect = None
    record_list = []

    delete_sql = StockData.get_delete_sql()
    insert_sql = StockData.get_insert_sql()

    if Utility.is_empty(stock_data_list):
        print("stock_data_list is empty, return")
        return

    try:
        connect = sqlite3.connect(Constants.DATA_DATABASE_ORION_DB)
        cursor = connect.cursor()

        cursor.execute(delete_sql, (period, stock_code))

        for stock_data in stock_data_list:
            now = datetime.now().strftime(Constants.DATE_TIME_FORMAT)

            if isinstance(stock_data, dict):
                stock_data_obj = StockData()
                stock_data_obj.set_stock_code(stock_code)
                stock_data_obj.set_date(stock_data['date'])
                stock_data_obj.set_time("00:00")
                stock_data_obj.set_period(period)
                stock_data_obj.set_open(stock_data['open'])
                stock_data_obj.set_high(stock_data['high'])
                stock_data_obj.set_low(stock_data['low'])
                stock_data_obj.set_close(stock_data['close'])
                stock_data_obj.set_volume(stock_data['volume'])
                stock_data_obj.set_created(now)
                stock_data_obj.set_modified(now)
            elif isinstance(stock_data, tuple):
                stock_data_obj = StockData(stock_data)
                stock_data_obj.set_modified(now)

            record = stock_data_obj.to_tuple(include_id=False)
            record_list.append(record)

        cursor.executemany(insert_sql, record_list)
        connect.commit()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()


def write_financial_data_to_database(stock_code, financial_data_list):
    connect = None
    record_list = []

    delete_sql = FinancialData.get_delete_sql()
    insert_sql = FinancialData.get_insert_sql()

    if Utility.is_empty(financial_data_list):
        print("financial_data_list is empty, return")
        return

    try:
        connect = sqlite3.connect(Constants.DATA_DATABASE_ORION_DB)
        cursor = connect.cursor()

        cursor.execute(delete_sql, (stock_code,))

        for financial_data in financial_data_list:
            now = datetime.now().strftime(Constants.DATE_TIME_FORMAT)

            if isinstance(financial_data, dict):
                financial_data_obj = FinancialData()
                financial_data_obj.set_stock_code(stock_code)
                financial_data_obj.set_date(financial_data['date'])
                financial_data_obj.set_book_value_per_share(financial_data['book_value_per_share'])
                financial_data_obj.set_cash_flow_per_share(financial_data['cash_flow_per_share'])
                financial_data_obj.set_total_current_assets(financial_data['total_current_assets'])
                financial_data_obj.set_total_assets(financial_data['total_assets'])
                financial_data_obj.set_total_long_term_liabilities(financial_data['total_long_term_liabilities'])
                financial_data_obj.set_main_business_income(financial_data['main_business_income'])
                financial_data_obj.set_financial_expenses(financial_data['financial_expenses'])
                financial_data_obj.set_net_profit(financial_data['net_profit'])
                financial_data_obj.set_net_profit_per_share(financial_data['net_profit_per_share'])
                financial_data_obj.set_created(now)
                financial_data_obj.set_modified(now)
            elif isinstance(financial_data, tuple):
                financial_data_obj = FinancialData(financial_data)
                financial_data_obj.set_modified(now)

            record = financial_data_obj.to_tuple(include_id=False)
            record_list.append(record)

        cursor.executemany(insert_sql, record_list)
        connect.commit()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()


def write_share_bonus_to_database(stock_code, share_bonus_list):
    connect = None
    record_list = []

    delete_sql = ShareBonus.get_delete_sql()
    insert_sql = ShareBonus.get_insert_sql()

    if Utility.is_empty(share_bonus_list):
        print("share_bonus_list is empty, return")
        return

    try:
        connect = sqlite3.connect(Constants.DATA_DATABASE_ORION_DB)
        cursor = connect.cursor()

        cursor.execute(delete_sql, (stock_code,))

        for share_bonus in share_bonus_list:
            now = datetime.now().strftime(Constants.DATE_TIME_FORMAT)

            share_bonus_obj = ShareBonus()
            share_bonus_obj.set_stock_code(stock_code)
            share_bonus_obj.set_date(share_bonus['date'])
            share_bonus_obj.set_dividend(share_bonus['dividend'])
            share_bonus_obj.set_r_date(share_bonus['r_date'])
            share_bonus_obj.set_created(now)
            share_bonus_obj.set_modified(now)

            record = share_bonus_obj.to_tuple(include_id=False)
            record_list.append(record)

        cursor.executemany(insert_sql, record_list)
        connect.commit()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()


def write_total_share_to_database(stock_code, total_share_list):
    connect = None
    record_list = []

    delete_sql = TotalShare.get_delete_sql()
    insert_sql = TotalShare.get_insert_sql()

    if Utility.is_empty(total_share_list):
        print("total_share_list is empty, return")
        return

    try:
        connect = sqlite3.connect(Constants.DATA_DATABASE_ORION_DB)
        cursor = connect.cursor()

        cursor.execute(delete_sql, (stock_code,))

        for total_share in total_share_list:
            now = datetime.now().strftime(Constants.DATE_TIME_FORMAT)

            total_share_obj = TotalShare()
            total_share_obj.set_stock_code(stock_code)
            total_share_obj.set_date(total_share['date'])
            total_share_obj.set_total_share(total_share['total_share'])
            total_share_obj.set_created(now)
            total_share_obj.set_modified(now)

            record = total_share_obj.to_tuple(include_id=False)
            record_list.append(record)

        cursor.executemany(insert_sql, record_list)
        connect.commit()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()


def write_share_holder_to_database(stock_code, share_holder_list_list):
    connect = None
    record_list = []

    delete_sql = ShareHolder.get_delete_sql()
    insert_sql = ShareHolder.get_insert_sql()

    if Utility.is_empty(share_holder_list_list):
        print("share_holder_list_list is empty, return")
        return

    try:
        connect = sqlite3.connect(Constants.DATA_DATABASE_ORION_DB)
        cursor = connect.cursor()

        cursor.execute(delete_sql, (stock_code,))

        for share_holder_list in share_holder_list_list:
            if Utility.is_empty(share_holder_list):
                print("share_holder_list is empty, return")
                continue

            for share_holder in share_holder_list:
                now = datetime.now().strftime(Constants.DATE_TIME_FORMAT)

                share_holder_obj = ShareHolder()
                share_holder_obj.set_stock_code(stock_code)
                share_holder_obj.set_date(share_holder['date'])
                share_holder_obj.set_type(share_holder['type'])
                share_holder_obj.set_number(share_holder['number'])
                share_holder_obj.set_hold(share_holder['hold'])
                share_holder_obj.set_ratio(share_holder['ratio'])
                share_holder_obj.set_created(now)
                share_holder_obj.set_modified(now)

                record = share_holder_obj.to_tuple(include_id=False)
                record_list.append(record)

        cursor.executemany(insert_sql, record_list)
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
        return "./data/stock/" + period + "/" + stock.get_code() + ".csv"


def get_financial_data_file_name(stock):
    if stock is None:
        return None
    else:
        return "./data/financial/" + stock.get_code() + ".csv"


def get_share_bonus_file_name(stock):
    if stock is None:
        return None
    else:
        return "./data/share_bonus/" + stock.get_code() + ".csv"


def get_share_holder_file_name(stock):
    if stock is None:
        return None
    else:
        return "./data/share_holder/" + stock.get_code() + ".csv"


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
    if Utility.is_empty(stock_tuple_list):
        return

    file_name = get_stock_file_name()

    field_name_tuple = tuple(("id", "classes",
                              "se", "code", "name", "pinyin",
                              "price", "change", "net", "volume", "value", "market_value",
                              "mark", "operation", "hold", "cost", "profit",
                              "roi", "roe", "pe", "rate", "pb",
                              "dividend", "dividend_yield", "dividend_ratio",
                              "total_share", "time_to_market", "created", "modified"))

    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name_tuple)
        writer.writeheader()

        for stock_tuple in stock_tuple_list:
            stock = Stock(stock_tuple)
            if stock is None:
                continue

            stock_dict = {"id": stock.get_id(), "classes": stock.get_classes(),
                          "se": stock.get_se(), "code": stock.get_code(), "name": stock.get_name(),
                          "pinyin": stock.get_pinyin(),
                          "price": stock.get_price(), "change": stock.get_change(), "net": stock.get_net(),
                          "volume": stock.get_volume(),
                          "value": stock.get_value(), "market_value": stock.get_market_value(),
                          "mark": stock.get_mark(), "operation": stock.get_operation(), "hold": stock.get_hold(),
                          "cost": stock.get_cost(),
                          "profit": stock.get_profit(),
                          "roi": stock.get_roi(), "roe": stock.get_roe(), "pe": stock.get_pe(),
                          "rate": stock.get_rate(), "pb": stock.get_pb(),
                          "dividend": stock.get_dividend(), "dividend_yield": stock.get_dividend_yield(),
                          "dividend_ratio": stock.get_dividend_ratio(),
                          "total_share": stock.get_total_share(), "time_to_market": stock.get_time_to_market(),
                          "created": stock.get_created(), "modified": stock.get_modified()}
            writer.writerow(stock_dict)


def write_stock_data_to_file(stock, stock_data_tuple_list, period=Constants.MONTH):
    if stock is None:
        return

    if Utility.is_empty(stock_data_tuple_list):
        return

    file_name = get_stock_data_file_name(stock, period)

    field_name_tuple = tuple(("date", "open", "high", "low", "close", "volume", "roi"))

    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name_tuple)
        writer.writeheader()

        for stock_data_tuple in stock_data_tuple_list:
            stock_data = StockData(stock_data_tuple)
            if stock_data is None:
                continue

            stock_data_dict = {"date": stock_data.date, "open": stock_data.open, "high": stock_data.high,
                               "low": stock_data.low, "close": stock_data.close, "volume": stock_data.volume,
                               "roi": stock_data.roi}
            writer.writerow(stock_data_dict)


def write_financial_data_to_file(stock, financial_data_tuple_list):
    if stock is None:
        return

    if Utility.is_empty(financial_data_tuple_list):
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
                              "net_profit_per_share",
                              "roe"))

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
                                   "roe": financial_data.roe,
                                   }
            writer.writerow(financial_data_dict)


def write_share_bonus_to_file(stock, share_bonus_tuple_list):
    if stock is None:
        return

    if Utility.is_empty(share_bonus_tuple_list):
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


def write_share_holder_to_file(stock, share_holder_tuple_list):
    if stock is None:
        return

    if Utility.is_empty(share_holder_tuple_list):
        return

    file_name = get_share_holder_file_name(stock)

    field_name_tuple = tuple(("date",
                              "number",
                              "ratio"))

    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name_tuple)
        writer.writeheader()

        for share_holder_tuple in share_holder_tuple_list:
            share_holder = ShareHolder(share_holder_tuple)
            if share_holder is None:
                continue

            share_holder_dict = {"date": share_holder.date,
                                 "number": share_holder.number,
                                 "ratio": share_holder.ratio,
                                 }
            writer.writerow(share_holder_dict)


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
        connect = sqlite3.connect(Constants.DATA_DATABASE_ORION_DB)
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
    if stock is None:
        return None

    return Utility.get_tuple_list_from_database("SELECT * FROM stock_data WHERE stock_code = ? AND period = ?  order "
                                                "by date desc", (stock.get_code(), period))


def read_financial_data_from_database(stock):
    if stock is None:
        return None

    return Utility.get_tuple_list_from_database("SELECT * FROM financial_data WHERE stock_code = ?  order by date desc",
                                                (stock.get_code(),))


def read_share_bonus_from_database(stock):
    if stock is None:
        return None

    return Utility.get_tuple_list_from_database("SELECT * FROM share_bonus WHERE stock_code = ?  order by date desc",
                                                (stock.get_code(),))


def read_total_share_from_database(stock):
    if stock is None:
        return None

    return Utility.get_tuple_list_from_database("SELECT * FROM total_share WHERE stock_code = ?  order by date desc",
                                                (stock.get_code(),))


def read_share_holder_from_database(stock):
    if stock is None:
        return None

    return Utility.get_tuple_list_from_database(
        "SELECT * FROM share_holder WHERE stock_code = ? AND type='机构汇总'  order by date desc",
        (stock.get_code(),))


def setup_total_share(financial_data_tuple_list, total_share_tuple_list):
    if Utility.is_empty(financial_data_tuple_list):
        return

    if Utility.is_empty(total_share_tuple_list):
        return

    j = 0
    for i in range(len(financial_data_tuple_list)):
        financial_data_tuple = financial_data_tuple_list[i]
        financial_data = FinancialData(financial_data_tuple)

        while j < len(total_share_tuple_list):
            total_share = TotalShare(total_share_tuple_list[j])
            if datetime.strptime(financial_data.get_date(), Constants.DATE_FORMAT) >= datetime.strptime(
                    total_share.get_date(), Constants.DATE_FORMAT):
                financial_data.set_total_share(total_share.get_total_share())
                financial_data_tuple_list[i] = financial_data.to_tuple(include_id=True)
                break
            else:
                j += 1


def setup_net_profit_per_share(financial_data_tuple_list):
    if Utility.is_empty(financial_data_tuple_list):
        return

    for i in range(len(financial_data_tuple_list)):
        financial_data_tuple = financial_data_tuple_list[i]
        financial_data = FinancialData(financial_data_tuple)
        financial_data.setup_net_profit_per_share()
        financial_data.setup_debt_to_net_assets_ratio()
        financial_data_tuple_list[i] = financial_data.to_tuple(include_id=True)


def setup_net_profit_per_share_in_year(financial_data_tuple_list):
    if Utility.is_empty(financial_data_tuple_list):
        return

    if len(financial_data_tuple_list) < Constants.SEASONS_IN_A_YEAR + 1:
        return

    for i in range(len(financial_data_tuple_list) - Constants.SEASONS_IN_A_YEAR):
        net_profit_per_share_in_year = 0
        for j in range(Constants.SEASONS_IN_A_YEAR):
            current = FinancialData(financial_data_tuple_list[i + j])
            prev = FinancialData(financial_data_tuple_list[i + j + 1])

            if current is None or prev is None:
                continue

            if current.get_total_share() == 0:
                continue

            if "03-31" in current.date:
                net_profit_per_share = current.get_net_profit() / current.get_total_share()
            else:
                net_profit_per_share = (current.get_net_profit() - prev.get_net_profit()) / current.get_total_share()

            net_profit_per_share_in_year += net_profit_per_share

        financial_data_tuple = financial_data_tuple_list[i]
        financial_data = FinancialData(financial_data_tuple)
        financial_data.set_net_profit_per_share_in_year(net_profit_per_share_in_year)
        financial_data_tuple_list[i] = financial_data.to_tuple(include_id=True)


def setup_rate(financial_data_tuple_list):
    if Utility.is_empty(financial_data_tuple_list):
        return

    if len(financial_data_tuple_list) < Constants.SEASONS_IN_A_YEAR + 1:
        return

    for i in range(len(financial_data_tuple_list) - Constants.SEASONS_IN_A_YEAR):
        financial_data = FinancialData(financial_data_tuple_list[i])
        prev = FinancialData(financial_data_tuple_list[i + Constants.SEASONS_IN_A_YEAR])

        if prev is None or prev.get_net_profit_per_share_in_year() == 0:
            continue

        rate = round(financial_data.get_net_profit_per_share_in_year() / prev.get_net_profit_per_share_in_year(),
                     Constants.DOUBLE_FIXED_DECIMAL)

        financial_data.set_rate(rate)
        financial_data_tuple_list[i] = financial_data.to_tuple(include_id=True)


def setup_roe(financial_data_tuple_list):
    if Utility.is_empty(financial_data_tuple_list):
        return

    if len(financial_data_tuple_list) < Constants.SEASONS_IN_A_YEAR + 1:
        return

    for i in range(len(financial_data_tuple_list) - Constants.SEASONS_IN_A_YEAR):
        financial_data = FinancialData(financial_data_tuple_list[i])
        prev = FinancialData(financial_data_tuple_list[i + Constants.SEASONS_IN_A_YEAR])

        if prev is None or prev.get_book_value_per_share() == 0:
            continue

        roe = round(100.0 * financial_data.get_net_profit_per_share_in_year() / prev.get_book_value_per_share(),
                    Constants.DOUBLE_FIXED_DECIMAL)
        financial_data.set_roe(roe)
        financial_data_tuple_list[i] = financial_data.to_tuple(include_id=True)


def setup_roi(stock_data_tuple_list, financial_data_tuple_list):
    if Utility.is_empty(stock_data_tuple_list):
        return

    if Utility.is_empty(financial_data_tuple_list):
        return

    j = 0
    for i in range(len(stock_data_tuple_list)):
        stock_data = StockData(stock_data_tuple_list[i])
        price = stock_data.get_close()
        if price == 0:
            continue

        while j < len(financial_data_tuple_list):
            financial_data = FinancialData(financial_data_tuple_list[j])
            if datetime.strptime(stock_data.get_date(), Constants.DATE_FORMAT) >= datetime.strptime(
                    financial_data.get_date(), Constants.DATE_FORMAT):
                pe = round(100.0 * financial_data.get_net_profit_per_share_in_year() / price,
                           Constants.DOUBLE_FIXED_DECIMAL)
                if financial_data.get_book_value_per_share() != 0:
                    pb = round(price / financial_data.get_book_value_per_share(), Constants.DOUBLE_FIXED_DECIMAL)
                # roi = round(financial_data.rate * financial_data.roe * pe * Constants.ROI_COEFFICIENT,
                #             Constants.DOUBLE_FIXED_DECIMAL)
                roi = round(financial_data.roe * pe * Constants.ROI_COEFFICIENT,
                            Constants.DOUBLE_FIXED_DECIMAL)
                if roi < 0:
                    roi = 0

                stock_data.set_pe(pe)
                stock_data.set_pb(pb)
                stock_data.set_roi(roi)
                stock_data_tuple_list[i] = stock_data.to_tuple(include_id=True)
                break
            else:
                j += 1


def analyze_financial_data(stock, financial_data_tuple_list):
    if stock is None:
        return stock

    if Utility.is_empty(financial_data_tuple_list):
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
    stock.setup_debt_to_net_assets_ratio()
    stock.setup_roe(financial_data_tuple_list)
    stock.setup_pe()
    stock.setup_pb()
    stock.setup_roi()
    stock.setup_market_value()

    return stock


def analyze_share_bonus(stock, share_bonus_tuple_list):
    total_divident = 0
    prev_year = None

    if stock is None:
        return stock

    if Utility.is_empty(share_bonus_tuple_list):
        return stock

    i = -1
    for share_bonus_tuple in share_bonus_tuple_list:
        i += 1

        if Utility.is_empty(share_bonus_tuple):
            break

        share_bonus = ShareBonus(share_bonus_tuple)
        if share_bonus is None:
            break

        if Utility.is_empty(share_bonus.date):
            break

        strings = share_bonus.date.split("-")
        if Utility.is_empty(strings):
            break

        year = strings[0]

        if prev_year is not None:
            if prev_year != year:
                break

        total_divident += float(share_bonus.dividend)

        if i == 0:
            stock.set_date(share_bonus.date)
            stock.set_r_date(share_bonus.r_date)

        stock.set_dividend(round(total_divident, Constants.DOUBLE_FIXED_DECIMAL))
        stock.setup_dividend_yield()
        stock.setup_dividend_ratio()

        prev_year = year

    return stock


def analyze():
    stock_tuple_list = read_stock_tuple_list_from_database()
    if Utility.is_empty(stock_tuple_list):
        print("stock_tuple_list is empty, return")
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

        if not check_out(stock):
            continue

        count += 1

        print(index, stock.get_code(), stock.get_name())

        stock_data_tuple_list = read_stock_data_from_database(stock)
        financial_data_tuple_list = read_financial_data_from_database(stock)
        share_bonus_tuple_list = read_share_bonus_from_database(stock)
        total_share_tuple_list = read_total_share_from_database(stock)
        share_holder_tuple_list = read_share_holder_from_database(stock)

        setup_total_share(financial_data_tuple_list, total_share_tuple_list)
        setup_net_profit_per_share(financial_data_tuple_list)
        setup_net_profit_per_share_in_year(financial_data_tuple_list)
        setup_rate(financial_data_tuple_list)
        setup_roe(financial_data_tuple_list)

        setup_roi(stock_data_tuple_list, financial_data_tuple_list)

        stock = analyze_financial_data(stock, financial_data_tuple_list)
        stock = analyze_share_bonus(stock, share_bonus_tuple_list)

        stock.update_to_database()
        write_financial_data_to_database(stock.get_code(), financial_data_tuple_list)
        write_stock_data_to_database(stock.get_code(), stock_data_tuple_list)

    print("analyze done, count=", count)


def select(where=None, order=None, sort=None):
    select_tuple_list = tuple()

    stock_tuple_list = read_stock_tuple_list_from_database(where, order, sort)
    write_stock_to_file(stock_tuple_list)

    stock_code_file = open(Constants.DATA_STOCK_LIST_CODE, "w")

    root = ET.Element("root")

    count = 0
    for stock_tuple in stock_tuple_list:
        stock = Stock(stock_tuple)

        if not check_out(stock):
            continue

        count = count + 1

        print(stock.to_string())

        stock_code_file.write(stock.get_code() + "\n")

        stock_element = ET.Element("stock")
        root.append(stock_element)

        if stock.get_se() is not None:
            stock_se = ET.SubElement(stock_element, "se")
            stock_se.text = stock.get_se()

        if stock.get_code() is not None:
            stock_code = ET.SubElement(stock_element, "code")
            stock_code.text = stock.get_code()

        if stock.get_name() is not None:
            stock_name = ET.SubElement(stock_element, "name")
            stock_name.text = stock.get_name()

    print("select done, count=", count)

    stock_code_file.close()

    tree = ET.ElementTree(root)
    with open(Constants.DATA_STOCK_LIST_XML, "wb") as files:
        tree.write(files)

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

    share_holder_tuple_list = read_share_holder_from_database(stock)
    write_share_holder_to_file(stock, share_holder_tuple_list)


def in_check_list(stock, check_list):
    result = False

    if stock is None:
        return result

    if Utility.is_empty(check_list):
        return result

    if stock.get_code() in check_list:
        result = True

    return result


def check_out(stock):
    result = False

    if stock is None:
        return result

    if exclude_private_owner:
        if in_check_list(stock, PrivateOwner.stock_list):
            return False

    if favorite_only:
        if in_check_list(stock, Favorite.stock_list):
            return True
        else:
            return False

    if stock_pool_only:
        if in_check_list(stock, StockPool.stock_list):
            return True
        else:
            return False

    if stock.is_special_treatment():
        # print(stock.mName, " is special treatment.")
        return False

    if stock.is_time_to_market_too_short():
        # print(stock.mName, " time to market too short.")
        return False

    result = True

    return result
