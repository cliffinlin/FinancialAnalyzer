# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime

from dateutil.relativedelta import relativedelta

import Constants
import DatabaseContract
from FinancialData import FinancialData


class Stock:
    def __init__(self, stock=None):
        self.mID = 0
        self.mClasses = ""
        self.mSymbol = ""
        self.mSE = ""
        self.mCode = ""
        self.mName = ""
        self.mPinyin = ""
        self.mMark = 0
        self.mPrice = 0
        self.mChange = 0
        self.mNet = 0
        self.mVolume = 0
        self.mValue = 0
        self.mOperation = 0
        self.mHold = 0
        self.mCost = 0
        self.mProfit = 0
        self.mTotalShare = 0
        self.mTotalAssets = 0
        self.mTotalLongTermLiabilities = 0
        self.mDebtToNetAssetsRatio = 0
        self.mBookValuePerShare = 0
        self.mCashFlowPerShare = 0
        self.mNetProfit = 0
        self.mNetProfitPerShare = 0
        self.mNetProfitPerShareInYear = 0
        self.mNetProfitPerShareLastYear = 0
        self.mRate = 0
        self.mRoi = 0
        self.mRoe = 0
        self.mPe = 0
        self.mPb = 0
        self.mDate = 0
        self.mDividend = 0
        self.mDividendYield = 0
        self.mDelta = 0
        self.mRDate = ""
        self.mTimeToMarket = ""
        self.mCreated = ""
        self.mModified = ""

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
            self.set_delta(stock[DatabaseContract.StockColumn.delta.value])
            self.set_r_date(stock[DatabaseContract.StockColumn.r_date.value])
            self.set_time_to_market(stock[DatabaseContract.StockColumn.time_to_market.value])
            self.set_created(stock[DatabaseContract.StockColumn.created.value])
            self.set_modified(stock[DatabaseContract.StockColumn.modified.value])

    def set_id(self, id):
        if id is not None:
            self.mID = id

    def set_classes(self, classes):
        if classes is not None:
            self.mClasses = classes

    def set_symbol(self, symbol):
        if symbol is not None:
            self.mSymbol = symbol

    def set_se(self, se):
        if se is not None:
            self.mSE = se

    def set_code(self, code):
        if code is not None:
            self.mCode = code

    def set_name(self, name):
        if name is not None:
            self.mName = name

    def set_pinyin(self, pinyin):
        if pinyin is not None:
            self.mPinyin = pinyin

    def set_mark(self, mark):
        if mark is not None:
            self.mMark = mark

    def set_price(self, price):
        if price is not None:
            self.mPrice = price

    def set_change(self, change):
        if change is not None:
            self.mChange = change

    def set_net(self, net):
        if net is not None:
            self.mNet = net

    def set_volume(self, volume):
        if volume is not None:
            self.mVolume = volume

    def set_value(self, value):
        if value is not None:
            self.mValue = value

    def set_operation(self, operation):
        if operation is not None:
            self.mOperation = operation

    def set_hold(self, hold):
        if hold is not None:
            self.mHold = hold

    def set_cost(self, cost):
        if cost is not None:
            self.mCost = cost

    def set_profit(self, profit):
        if profit is not None:
            self.mProfit = profit

    def set_total_share(self, total_share):
        if total_share is not None:
            self.mTotalShare = total_share

    def set_total_assets(self, total_assets):
        if total_assets is not None:
            self.mTotalAssets = total_assets

    def set_total_long_term_liabilities(self, total_long_term_liabilities):
        if total_long_term_liabilities is not None:
            self.mTotalLongTermLiabilities = total_long_term_liabilities

    def set_debt_to_net_assets_ratio(self, debt_to_net_assets_ratio):
        if debt_to_net_assets_ratio is not None:
            self.mDebtToNetAssetsRatio = debt_to_net_assets_ratio

    def set_book_value_per_share(self, book_value_per_share):
        if book_value_per_share is not None:
            self.mBookValuePerShare = book_value_per_share

    def set_cash_flow_per_share(self, cash_flow_per_share):
        if cash_flow_per_share is not None:
            self.mCashFlowPerShare = cash_flow_per_share

    def set_net_profit(self, net_profit):
        if net_profit is not None:
            self.mNetProfit = net_profit

    def set_net_profit_per_share(self, net_profit_per_share):
        if net_profit_per_share is not None:
            self.mNetProfitPerShare = net_profit_per_share

    def set_net_profit_per_share_in_year(self, net_profit_per_share_in_year):
        if net_profit_per_share_in_year is not None:
            self.mNetProfitPerShareInYear = net_profit_per_share_in_year

    def set_net_profit_per_share_last_year(self, net_profit_per_share_last_year):
        if net_profit_per_share_last_year is not None:
            self.mNetProfitPerShareLastYear = net_profit_per_share_last_year

    def set_rate(self, rate):
        if rate is not None:
            self.mRate = rate

    def set_roi(self, roi):
        if roi is not None:
            self.mRoi = roi

    def set_roe(self, roe):
        if roe is not None:
            self.mRoe = roe

    def set_pe(self, pe):
        if pe is not None:
            self.mPe = pe

    def set_pb(self, pb):
        if pb is not None:
            self.mPb = pb

    def set_date(self, date):
        if date is not None:
            self.mDate = date

    def set_dividend(self, dividend):
        if dividend is not None:
            self.mDividend = dividend

    def set_dividend_yield(self, dividend_yield):
        if dividend_yield is not None:
            self.mDividendYield = dividend_yield

    def set_delta(self, delta):
        if delta is not None:
            self.mDelta = delta

    def set_r_date(self, r_date):
        if r_date is not None:
            self.mRDate = r_date

    def set_time_to_market(self, time_to_market):
        if time_to_market is not None:
            self.mTimeToMarket = time_to_market

    def set_created(self, created):
        if created is not None:
            self.mCreated = created

    def set_modified(self, modified):
        if modified is not None:
            self.mModified = modified

    def setup_net_profit_per_share(self):
        if self.mTotalShare == 0:
            return

        self.mNetProfitPerShare = round(self.mNetProfit / self.mTotalShare, Constants.DOUBLE_FIXED_DECIMAL)

    def setup_net_profit_per_share_in_year(self, financial_data_tuple_list):
        if self.mTotalShare == 0:
            return

        if financial_data_tuple_list is None:
            return

        if len(financial_data_tuple_list) < Constants.SEASONS_IN_A_YEAR + 1:
            return

        self.mNetProfitPerShareInYear = 0

        for i in range(0, Constants.SEASONS_IN_A_YEAR):
            financial_data = FinancialData(financial_data_tuple_list[i])
            prev = FinancialData(financial_data_tuple_list[i + 1])

            if financial_data is None or prev is None:
                break

            if "03-31" in financial_data.date:
                net_profit_per_share = financial_data.net_profit / self.mTotalShare
            else:
                net_profit_per_share = (financial_data.net_profit - prev.net_profit) / self.mTotalShare

            self.mNetProfitPerShareInYear += net_profit_per_share

    def setup_net_profit_per_share_last_year(self, financial_data_tuple_list):
        if self.mTotalShare == 0:
            return

        if financial_data_tuple_list is None:
            return

        if len(financial_data_tuple_list) < 2 * Constants.SEASONS_IN_A_YEAR + 1:
            return

        self.mNetProfitPerShareLastYear = 0

        for i in range(Constants.SEASONS_IN_A_YEAR, 2 * Constants.SEASONS_IN_A_YEAR):
            financial_data = FinancialData(financial_data_tuple_list[i])
            prev = FinancialData(financial_data_tuple_list[i + 1])

            if financial_data is None or prev is None:
                break

            if "03-31" in financial_data.date:
                net_profit_per_share = financial_data.net_profit / self.mTotalShare
            else:
                net_profit_per_share = (financial_data.net_profit - prev.net_profit) / self.mTotalShare

            self.mNetProfitPerShareLastYear += net_profit_per_share

    def setup_rate(self):
        if self.mNetProfitPerShareLastYear == 0:
            return

        self.mRate = round(self.mNetProfitPerShareInYear / self.mNetProfitPerShareLastYear,
                           Constants.DOUBLE_FIXED_DECIMAL)

    def setup_debt_to_net_assets_ratio(self):
        if self.mTotalLongTermLiabilities == 0:
            return

        if self.mTotalShare == 0:
            return

        if self.mBookValuePerShare == 0:
            return

        self.mDebtToNetAssetsRatio = self.mTotalLongTermLiabilities / self.mTotalShare / self.mBookValuePerShare

    def setup_roi(self):
        self.mRoi = round(self.mRate * self.mRoe * self.mPe * Constants.ROI_COEFFICIENT, Constants.DOUBLE_FIXED_DECIMAL)
        # self.mRoi = round(self.mRoe * self.mPe * Constants.ROI_COEFFICIENT, Constants.DOUBLE_FIXED_DECIMAL)

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

        self.mRoe = round(100.0 * self.mNetProfitPerShareInYear / book_value_per_share, Constants.DOUBLE_FIXED_DECIMAL)

    def setup_pe(self):
        if self.mPrice == 0:
            return

        self.mPe = round(100.0 * self.mNetProfitPerShareInYear / self.mPrice, Constants.DOUBLE_FIXED_DECIMAL)

    def setup_pb(self):
        if self.mBookValuePerShare == 0:
            return

        self.mPb = round(self.mPrice / self.mBookValuePerShare, Constants.DOUBLE_FIXED_DECIMAL)

    def setup_dividend_yield(self):
        if self.mPrice == 0:
            return

        self.mDividendYield = round(100.0 * self.mDividend / 10.0 / self.mPrice, Constants.DOUBLE_FIXED_DECIMAL)

    def setup_delta(self):
        if self.mDividend == 0:
            return
        if self.mNetProfitPerShareInYear <= 0:
            return

        self.mDelta = round(100.0 * self.mDividend / 10.0 / self.mNetProfitPerShareInYear, Constants.DOUBLE_FIXED_DECIMAL)

    def get_insert_tuple(self):
        return tuple((self.mSymbol, self.mSE, self.mCode, self.mName,
                      self.mPrice, self.mChange, self.mNet,
                      self.mCreated, self.mModified))

    def get_update_tuple(self):
        return tuple((self.mSymbol, self.mSE, self.mCode, self.mName,
                      self.mPrice, self.mChange, self.mNet,
                      self.mModified, self.mCode))

    def is_special_treatment(self):
        result = False

        if "ST" in self.mName:
            result = True

        return result

    def is_time_to_market_too_short(self):
        result = False

        if self.mTimeToMarket is None:
            return result

        if len(self.mTimeToMarket) < len(Constants.DATE_FORMAT):
            return result

        time_to_market_min = datetime.now() - relativedelta(years=Constants.TIME_TO_MARKET_YEAR_MIN)
        time_to_market = datetime.strptime(self.mTimeToMarket, Constants.DATE_FORMAT)

        if time_to_market > time_to_market_min:
            result = True

        return result

    def to_string(self):
        result = "\"" + self.mCode + "\"," + " #"\
                + self.mName + " " \
                + "roi=" + str(self.mRoi) + " " \
                + "roe=" + str(self.mRoe) + " " \
                + "1/pe=" + str(self.mPe) + " " \
                + "rate=" + str(self.mRate) + " " \
                + "pb=" + str(self.mPb) + " " \
                + "dividend=" + str(self.mDividend) + " " \
                + "yield=" + str(self.mDividendYield) + "% " \
                + "delta=" + str(self.mDelta) + "%"

        return result

    def update_to_database(self):
        connect = None
        sql_update = "UPDATE stock SET" \
                     " classes=?, pinyin=?," \
                     " mark=?, operation=?," \
                     " total_share=?, total_assets=?, " \
                     " total_long_term_liabilities=?, debt_to_net_assets_ratio=?, " \
                     " book_value_per_share=?, cash_flow_per_share=?, " \
                     " net_profit=?, net_profit_per_share=?, " \
                     " net_profit_per_share_in_year=?, net_profit_per_share_last_year=?, " \
                     " rate=?, roi=?, roe=?, " \
                     " pe=?, pb=?," \
                     " date=?, dividend=?," \
                     " dividend_yield=?, delta=?," \
                     " r_date=?, time_to_market=? WHERE code=?"

        try:
            connect = sqlite3.connect(DatabaseContract.DATABASE_FILE_NAME)
            cursor = connect.cursor()
            cursor.execute(sql_update, (self.mClasses, self.mPinyin,
                                        self.mMark, self.mOperation,
                                        self.mTotalShare, self.mTotalAssets,
                                        self.mTotalLongTermLiabilities, self.mDebtToNetAssetsRatio,
                                        self.mBookValuePerShare, self.mCashFlowPerShare,
                                        self.mNetProfit, self.mNetProfitPerShare,
                                        self.mNetProfitPerShareInYear, self.mNetProfitPerShareLastYear,
                                        self.mRate, self.mRoi, self.mRoe,
                                        self.mPe, self.mPb,
                                        self.mDate, self.mDividend,
                                        self.mDividendYield, self.mDelta,
                                        self.mRDate, self.mTimeToMarket, self.mCode))
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
