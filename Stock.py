# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime

from dateutil.relativedelta import relativedelta

import Constant
import DatabaseContract


class Stock:
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
            self.set_classes(stock[DatabaseContract.StockColumn.classes.value])
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
            self.set_operation(stock[DatabaseContract.StockColumn.operation.value])
            self.set_hold(stock[DatabaseContract.StockColumn.hold.value])
            self.set_cost(stock[DatabaseContract.StockColumn.cost.value])
            self.set_profit(stock[DatabaseContract.StockColumn.profit.value])
            self.set_total_share(stock[DatabaseContract.StockColumn.total_share.value])
            self.set_roe(stock[DatabaseContract.StockColumn.roe.value])
            self.set_rate(stock[DatabaseContract.StockColumn.rate.value])
            self.set_valuation(stock[DatabaseContract.StockColumn.valuation.value])
            self.set_discount(stock[DatabaseContract.StockColumn.discount.value])
            self.set_pe(stock[DatabaseContract.StockColumn.pe.value])
            self.set_pb(stock[DatabaseContract.StockColumn.pb.value])
            self.set_dividend(stock[DatabaseContract.StockColumn.dividend.value])
            self.set_dividend_yield(stock[DatabaseContract.StockColumn.dividend_yield.value])
            self.set_delta(stock[DatabaseContract.StockColumn.delta.value])
            self.set_time_to_market(stock[DatabaseContract.StockColumn.time_to_market.value])
            self.set_created(stock[DatabaseContract.StockColumn.created.value])
            self.set_modified(stock[DatabaseContract.StockColumn.modified.value])

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

    def is_special_treatment(self):
        result = False

        if "ST" in self.name:
            result = True

        return result

    def is_time_to_market_too_short(self):
        result = False

        if self.time_to_market is None:
            return result

        if len(self.time_to_market) < len(Constant.DATE_FORMAT):
            return result

        time_to_market_min = datetime.now() - relativedelta(years=Constant.TIME_TO_MARKET_YEAR_MIN)
        time_to_market = datetime.strptime(self.time_to_market, Constant.DATE_FORMAT)

        if time_to_market > time_to_market_min:
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
            connect = sqlite3.connect(DatabaseContract.DATABASE_FILE_NAME)
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
