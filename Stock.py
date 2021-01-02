# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime

from dateutil.relativedelta import relativedelta

import Constants
import DatabaseContract
from FinancialData import FinancialData


class Stock:
    def __init__(self, stock=None):
        self.id = 0
        self.classes = ""
        self.symbol = ""
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
        self.market_value = 0
        self.operation = 0
        self.hold = 0
        self.cost = 0
        self.profit = 0
        self.total_share = 0
        self.total_assets = 0
        self.total_long_term_liabilities = 0
        self.debt_to_net_assets_ratio = 0
        self.book_value_per_share = 0
        self.cash_flow_per_share = 0
        self.net_profit = 0
        self.net_profit_per_share = 0
        self.net_profit_per_share_in_year = 0
        self.net_profit_per_share_last_year = 0
        self.rate = 0
        self.roi = 0
        self.roe = 0
        self.pe = 0
        self.pb = 0
        self.date = 0
        self.dividend = 0
        self.dividend_yield = 0
        self.dividend_ratio = 0
        self.r_date = ""
        self.time_to_market = ""
        self.created = ""
        self.modified = ""

        if isinstance(stock, dict):
            se = stock["symbol"][0:2]

            self.set_symbol(stock['symbol'])
            self.set_se(se)
            self.set_code(stock['code'])
            self.set_name(stock['name'])
            self.set_price(stock['price'])
            self.set_change(stock['change'])
            self.set_net(stock['net'])
        elif isinstance(stock, tuple):
            self.set_id(stock[DatabaseContract.StockColumn.id.value])
            self.set_classes(stock[DatabaseContract.StockColumn.classes.value])
            self.set_symbol(stock[DatabaseContract.StockColumn.symbol.value])
            self.set_se(stock[DatabaseContract.StockColumn.se.value])
            self.set_code(stock[DatabaseContract.StockColumn.code.value])
            self.set_name(stock[DatabaseContract.StockColumn.name.value])
            self.set_pinyin(stock[DatabaseContract.StockColumn.pinyin.value])
            self.set_mark(stock[DatabaseContract.StockColumn.mark.value])
            self.set_price(stock[DatabaseContract.StockColumn.price.value])
            self.set_change(stock[DatabaseContract.StockColumn.change.value])
            self.set_net(stock[DatabaseContract.StockColumn.net.value])
            self.set_volume(stock[DatabaseContract.StockColumn.volume.value])
            self.set_value(stock[DatabaseContract.StockColumn.value.value])
            self.set_market_value(stock[DatabaseContract.StockColumn.market_value.value])
            self.set_operation(stock[DatabaseContract.StockColumn.operation.value])
            self.set_hold(stock[DatabaseContract.StockColumn.hold.value])
            self.set_cost(stock[DatabaseContract.StockColumn.cost.value])
            self.set_profit(stock[DatabaseContract.StockColumn.profit.value])
            self.set_total_share(stock[DatabaseContract.StockColumn.total_share.value])
            self.set_total_assets(stock[DatabaseContract.StockColumn.total_assets.value])
            self.set_total_long_term_liabilities(stock[DatabaseContract.StockColumn.total_long_term_liabilities.value])
            self.set_debt_to_net_assets_ratio(stock[DatabaseContract.StockColumn.debt_to_net_assets_ratio.value])
            self.set_book_value_per_share(stock[DatabaseContract.StockColumn.book_value_per_share.value])
            self.set_cash_flow_per_share(stock[DatabaseContract.StockColumn.cash_flow_per_share.value])
            self.set_net_profit(stock[DatabaseContract.StockColumn.net_profit.value])
            self.set_net_profit_per_share(stock[DatabaseContract.StockColumn.net_profit_per_share.value])
            self.set_net_profit_per_share_in_year(
                stock[DatabaseContract.StockColumn.net_profit_per_share_in_year.value])
            self.set_net_profit_per_share_last_year(
                stock[DatabaseContract.StockColumn.net_profit_per_share_last_year.value])
            self.set_rate(stock[DatabaseContract.StockColumn.rate.value])
            self.set_roi(stock[DatabaseContract.StockColumn.roi.value])
            self.set_roe(stock[DatabaseContract.StockColumn.roe.value])
            self.set_pe(stock[DatabaseContract.StockColumn.pe.value])
            self.set_pb(stock[DatabaseContract.StockColumn.pb.value])
            self.set_date(stock[DatabaseContract.StockColumn.date.value])
            self.set_dividend(stock[DatabaseContract.StockColumn.dividend.value])
            self.set_dividend_yield(stock[DatabaseContract.StockColumn.dividend_yield.value])
            self.set_dividend_ratio(stock[DatabaseContract.StockColumn.dividend_ratio.value])
            self.set_r_date(stock[DatabaseContract.StockColumn.r_date.value])
            self.set_time_to_market(stock[DatabaseContract.StockColumn.time_to_market.value])
            self.set_created(stock[DatabaseContract.StockColumn.created.value])
            self.set_modified(stock[DatabaseContract.StockColumn.modified.value])

    def get_id(self):
        return self.id

    def set_id(self, id):
        if id is not None:
            self.id = id

    def get_classes(self):
        return self.classes

    def set_classes(self, classes):
        if classes is not None:
            self.classes = classes

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        if symbol is not None:
            self.symbol = symbol

    def get_se(self):
        return self.se

    def set_se(self, se):
        if se is not None:
            self.se = se

    def get_code(self):
        return self.code

    def set_code(self, code):
        if code is not None:
            self.code = code

    def get_name(self):
        return self.name

    def set_name(self, name):
        if name is not None:
            self.name = name

    def get_pinyin(self):
        return self.pinyin

    def set_pinyin(self, pinyin):
        if pinyin is not None:
            self.pinyin = pinyin

    def get_mark(self):
        return self.mark

    def set_mark(self, mark):
        if mark is not None:
            self.mark = mark

    def get_price(self):
        return self.price

    def set_price(self, price):
        if price is not None:
            self.price = price

    def get_change(self):
        return self.change

    def set_change(self, change):
        if change is not None:
            self.change = change

    def get_net(self):
        return self.net

    def set_net(self, net):
        if net is not None:
            self.net = net

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        if volume is not None:
            self.volume = volume

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value is not None:
            self.value = value

    def get_market_value(self):
        return self.market_value

    def set_market_value(self, market_value):
        if market_value is not None:
            self.market_value = market_value

    def get_operation(self):
        return self.operation

    def set_operation(self, operation):
        if operation is not None:
            self.operation = operation

    def get_hold(self):
        return self.hold

    def set_hold(self, hold):
        if hold is not None:
            self.hold = hold

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        if cost is not None:
            self.cost = cost

    def get_profit(self):
        return self.profit

    def set_profit(self, profit):
        if profit is not None:
            self.profit = profit

    def get_total_share(self):
        return self.total_share

    def set_total_share(self, total_share):
        if total_share is not None:
            self.total_share = total_share

    def get_total_assets(self):
        return self.total_assets

    def set_total_assets(self, total_assets):
        if total_assets is not None:
            self.total_assets = total_assets

    def get_total_long_term_liabilities(self):
        return self.total_long_term_liabilities

    def set_total_long_term_liabilities(self, total_long_term_liabilities):
        if total_long_term_liabilities is not None:
            self.total_long_term_liabilities = total_long_term_liabilities

    def get_debt_to_net_assets_ratio(self):
        return self.debt_to_net_assets_ratio

    def set_debt_to_net_assets_ratio(self, debt_to_net_assets_ratio):
        if debt_to_net_assets_ratio is not None:
            self.debt_to_net_assets_ratio = debt_to_net_assets_ratio

    def get_book_value_per_share(self):
        return self.book_value_per_share

    def set_book_value_per_share(self, book_value_per_share):
        if book_value_per_share is not None:
            self.book_value_per_share = book_value_per_share

    def get_cash_flow_per_share(self):
        return self.cash_flow_per_share

    def set_cash_flow_per_share(self, cash_flow_per_share):
        if cash_flow_per_share is not None:
            self.cash_flow_per_share = cash_flow_per_share

    def get_net_profit(self):
        return self.net_profit

    def set_net_profit(self, net_profit):
        if net_profit is not None:
            self.net_profit = net_profit

    def get_net_profit_per_share(self):
        return self.net_profit_per_share

    def set_net_profit_per_share(self, net_profit_per_share):
        if net_profit_per_share is not None:
            self.net_profit_per_share = net_profit_per_share

    def get_net_profit_per_share_in_year(self):
        return self.net_profit_per_share_in_year

    def set_net_profit_per_share_in_year(self, net_profit_per_share_in_year):
        if net_profit_per_share_in_year is not None:
            self.net_profit_per_share_in_year = net_profit_per_share_in_year

    def get_net_profit_per_share_last_year(self):
        return self.net_profit_per_share_last_year

    def set_net_profit_per_share_last_year(self, net_profit_per_share_last_year):
        if net_profit_per_share_last_year is not None:
            self.net_profit_per_share_last_year = net_profit_per_share_last_year

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        if rate is not None:
            self.rate = rate

    def get_roi(self):
        return self.roi

    def set_roi(self, roi):
        if roi is not None:
            self.roi = roi

    def get_roe(self):
        return self.roe

    def set_roe(self, roe):
        if roe is not None:
            self.roe = roe

    def get_pe(self):
        return self.pe

    def set_pe(self, pe):
        if pe is not None:
            self.pe = pe

    def get_pb(self):
        return self.pb

    def set_pb(self, pb):
        if pb is not None:
            self.pb = pb

    def get_date(self):
        return self.date

    def set_date(self, date):
        if date is not None:
            self.date = date

    def get_dividend(self):
        return self.dividend

    def set_dividend(self, dividend):
        if dividend is not None:
            self.dividend = dividend

    def get_dividend_yield(self):
        return self.dividend_yield

    def set_dividend_yield(self, dividend_yield):
        if dividend_yield is not None:
            self.dividend_yield = dividend_yield

    def get_dividend_ratio(self):
        return self.dividend_ratio

    def set_dividend_ratio(self, dividend_ratio):
        if dividend_ratio is not None:
            self.dividend_ratio = dividend_ratio

    def get_r_date(self):
        return self.r_date

    def set_r_date(self, r_date):
        if r_date is not None:
            self.r_date = r_date

    def get_time_to_market(self):
        return self.time_to_market

    def set_time_to_market(self, time_to_market):
        if time_to_market is not None:
            self.time_to_market = time_to_market

    def get_created(self):
        return self.created

    def set_created(self, created):
        if created is not None:
            self.created = created

    def get_modified(self):
        return self.modified

    def set_modified(self, modified):
        if modified is not None:
            self.modified = modified

    def setup_net_profit_per_share(self):
        if self.total_share == 0:
            return

        self.net_profit_per_share = round(self.net_profit / self.total_share, Constants.DOUBLE_FIXED_DECIMAL)

    def setup_net_profit_per_share_in_year(self, financial_data_tuple_list):
        if self.total_share == 0:
            return

        if financial_data_tuple_list is None:
            return

        if len(financial_data_tuple_list) < Constants.SEASONS_IN_A_YEAR + 1:
            return

        self.net_profit_per_share_in_year = 0

        for i in range(0, Constants.SEASONS_IN_A_YEAR):
            financial_data = FinancialData(financial_data_tuple_list[i])
            prev = FinancialData(financial_data_tuple_list[i + 1])

            if financial_data is None or prev is None:
                break

            if "03-31" in financial_data.date:
                net_profit_per_share = financial_data.net_profit / self.total_share
            else:
                net_profit_per_share = (financial_data.net_profit - prev.net_profit) / self.total_share

            self.net_profit_per_share_in_year += net_profit_per_share

    def setup_net_profit_per_share_last_year(self, financial_data_tuple_list):
        if self.total_share == 0:
            return

        if financial_data_tuple_list is None:
            return

        if len(financial_data_tuple_list) < 2 * Constants.SEASONS_IN_A_YEAR + 1:
            return

        self.net_profit_per_share_last_year = 0

        for i in range(Constants.SEASONS_IN_A_YEAR, 2 * Constants.SEASONS_IN_A_YEAR):
            financial_data = FinancialData(financial_data_tuple_list[i])
            prev = FinancialData(financial_data_tuple_list[i + 1])

            if financial_data is None or prev is None:
                break

            if "03-31" in financial_data.date:
                net_profit_per_share = financial_data.net_profit / self.total_share
            else:
                net_profit_per_share = (financial_data.net_profit - prev.net_profit) / self.total_share

            self.net_profit_per_share_last_year += net_profit_per_share

    def setup_rate(self):
        if self.net_profit_per_share_last_year == 0:
            return

        self.rate = round(self.net_profit_per_share_in_year / self.net_profit_per_share_last_year,
                           Constants.DOUBLE_FIXED_DECIMAL)

    def setup_debt_to_net_assets_ratio(self):
        if self.total_long_term_liabilities == 0:
            return

        if self.total_share == 0:
            return

        if self.book_value_per_share == 0:
            return

        self.debt_to_net_assets_ratio = self.total_long_term_liabilities / self.total_share / self.book_value_per_share

    def setup_roi(self):
        self.roi = round(self.rate * self.roe * self.pe * Constants.ROI_COEFFICIENT, Constants.DOUBLE_FIXED_DECIMAL)

    def setup_roe(self, financial_data_tuple_list):
        if financial_data_tuple_list is None:
            return

        if len(financial_data_tuple_list) < Constants.SEASONS_IN_A_YEAR + 1:
            return

        financial_data = FinancialData(financial_data_tuple_list[Constants.SEASONS_IN_A_YEAR])
        if financial_data is None:
            return

        book_value_per_share = financial_data.book_value_per_share
        if book_value_per_share == 0:
            return

        self.roe = round(100.0 * self.net_profit_per_share_in_year / book_value_per_share, Constants.DOUBLE_FIXED_DECIMAL)

    def setup_market_value(self):
        if self.price == 0:
            self.market_value = 0
            return

        self.market_value = round(self.price * self.total_share / Constants.DOUBLE_CONSTANT_WAN / Constants.DOUBLE_CONSTANT_WAN, Constants.DOUBLE_FIXED_DECIMAL)

    def setup_pe(self):
        if self.price == 0:
            return

        self.pe = round(100.0 * self.net_profit_per_share_in_year / self.price, Constants.DOUBLE_FIXED_DECIMAL)

    def setup_pb(self):
        if self.book_value_per_share == 0:
            return

        self.pb = round(self.price / self.book_value_per_share, Constants.DOUBLE_FIXED_DECIMAL)

    def setup_dividend_yield(self):
        if self.price == 0:
            return

        self.dividend_yield = round(100.0 * self.dividend / 10.0 / self.price, Constants.DOUBLE_FIXED_DECIMAL)

    def setup_dividend_ratio(self):
        if self.dividend == 0:
            return
        if self.net_profit_per_share_in_year <= 0:
            return

        self.dividend_ratio = round(100.0 * self.dividend / 10.0 / self.net_profit_per_share_in_year,
                            Constants.DOUBLE_FIXED_DECIMAL)

    def get_insert_tuple(self):
        return tuple((self.symbol, self.se, self.code, self.name,
                      self.price, self.change, self.net,
                      self.created, self.modified))

    def get_update_tuple(self):
        return tuple((self.symbol, self.se, self.code, self.name,
                      self.price, self.change, self.net,
                      self.modified, self.code))

    def is_special_treatment(self):
        result = False

        if "ST" in self.name:
            result = True

        return result

    def is_time_to_market_too_short(self):
        result = False

        if self.time_to_market is None:
            return result

        if len(self.time_to_market) < len(Constants.DATE_FORMAT):
            return result

        time_to_market_min = datetime.now() - relativedelta(years=Constants.TIME_TO_MARKET_YEAR_MIN)
        time_to_market = datetime.strptime(self.time_to_market, Constants.DATE_FORMAT)

        if time_to_market > time_to_market_min:
            result = True

        return result

    def to_string(self):
        result = "\"" + self.code + "\"," + " #" \
                 + self.name + " " \
                 + "roi=" + str(self.roi) + " " \
                 + "roe=" + str(self.roe) + " " \
                 + "1/pe=" + str(self.pe) + " " \
                 + "rate=" + str(self.rate) + " " \
                 + "pb=" + str(self.pb) + " " \
                 + "dividend=" + str(self.dividend) + " " \
                 + "yield=" + str(self.dividend_yield) + "% " \
                 + "dividend_ratio=" + str(self.dividend_ratio) + "% " \
                 + "market_value=" + str(self.market_value)

        return result

    def update_to_database(self):
        connect = None
        sql_update = "UPDATE stock SET" \
                     " classes=?, pinyin=?," \
                     " mark=?, operation=?," \
                     " market_value=?," \
                     " total_share=?, total_assets=?, " \
                     " total_long_term_liabilities=?, debt_to_net_assets_ratio=?, " \
                     " book_value_per_share=?, cash_flow_per_share=?, " \
                     " net_profit=?, net_profit_per_share=?, " \
                     " net_profit_per_share_in_year=?, net_profit_per_share_last_year=?, " \
                     " rate=?, roi=?, roe=?, " \
                     " pe=?, pb=?," \
                     " date=?, dividend=?," \
                     " dividend_yield=?, dividend_ratio=?," \
                     " r_date=?, time_to_market=? WHERE code=?"

        try:
            connect = sqlite3.connect(Constants.DATA_DATABASE_ORION_DB)
            cursor = connect.cursor()
            cursor.execute(sql_update, (self.classes, self.pinyin,
                                        self.mark, self.operation,
                                        self.market_value,
                                        self.total_share, self.total_assets,
                                        self.total_long_term_liabilities, self.debt_to_net_assets_ratio,
                                        self.book_value_per_share, self.cash_flow_per_share,
                                        self.net_profit, self.net_profit_per_share,
                                        self.net_profit_per_share_in_year, self.net_profit_per_share_last_year,
                                        self.rate, self.roi, self.roe,
                                        self.pe, self.pb,
                                        self.date, self.dividend,
                                        self.dividend_yield, self.dividend_ratio,
                                        self.r_date, self.time_to_market, self.code))
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
                     "symbol, se, code, name, " \
                     "price, change, net, " \
                     "created, modified" \
                     ") VALUES(" \
                     "?,?,?,?," \
                     "?,?,?," \
                     "?,?)"
        return insert_sql

    @staticmethod
    def get_update_sql():
        update_sql = "UPDATE stock SET " \
                     "symbol=?, se=?, code=?, name=?, " \
                     "price=?, change=?, net=?, " \
                     "modified=? " \
                     " WHERE " \
                     "code=?"
        return update_sql
