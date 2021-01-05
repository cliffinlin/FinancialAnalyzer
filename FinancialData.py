# -*- coding: utf-8 -*-
import Constants
import DatabaseContract
import Utility


class FinancialData:
    def __init__(self, financial_data_tuple=None):
        self.id = 0
        self.stock_code = ""
        self.date = ""
        self.book_value_per_share = 0
        self.cash_flow_per_share = 0
        self.total_share = 0
        self.total_current_assets = 0
        self.total_assets = 0
        self.total_long_term_liabilities = 0
        self.debt_to_net_assets_ratio = 0
        self.main_business_income = 0
        self.financial_expenses = 0
        self.net_profit = 0
        self.net_profit_per_share = 0
        self.net_profit_per_share_in_year = 0
        self.rate = 0
        self.roi = 0
        self.roe = 0
        self.pe = 0
        self.pb = 0
        self.dividend = 0
        self.dividend_yield = 0
        self.dividend_ratio = 0
        self.created = ""
        self.modified = ""

        if financial_data_tuple is None:
            return

        self.set_id(financial_data_tuple[0])
        self.set_stock_code(financial_data_tuple[DatabaseContract.FinancialDataColumn.stock_code.value])
        self.set_date(financial_data_tuple[DatabaseContract.FinancialDataColumn.date.value])
        self.set_book_value_per_share(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.book_value_per_share.value])
        self.set_cash_flow_per_share(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.cash_flow_per_share.value])
        self.set_total_share(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.total_share.value])
        self.set_total_current_assets(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.total_current_assets.value])
        self.set_total_assets(financial_data_tuple[DatabaseContract.FinancialDataColumn.total_assets.value])
        self.set_total_long_term_liabilities(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.total_long_term_liabilities.value])
        self.set_debt_to_net_assets_ratio(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.debt_to_net_assets_ratio.value])
        self.set_main_business_income(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.main_business_income.value])
        self.set_financial_expenses(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.financial_expenses.value])
        self.set_net_profit(financial_data_tuple[DatabaseContract.FinancialDataColumn.net_profit.value])
        self.set_net_profit_per_share(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.net_profit_per_share.value])
        self.set_net_profit_per_share_in_year(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.net_profit_per_share_in_year.value])
        self.set_rate(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.rate.value])
        self.set_roi(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.roi.value])
        self.set_roe(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.roe.value])
        self.set_pe(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.pe.value])
        self.set_pb(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.pb.value])
        self.set_dividend(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.dividend.value])
        self.set_dividend_yield(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.dividend_yield.value])
        self.set_dividend_ratio(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.dividend_ratio.value])
        self.set_created(financial_data_tuple[DatabaseContract.FinancialDataColumn.created.value])
        self.set_modified(financial_data_tuple[DatabaseContract.FinancialDataColumn.modified.value])

    def get_id(self):
        return self.id

    def set_id(self, id):
        if id is not None:
            self.id = id

    def get_stock_code(self):
        return self.stock_code

    def set_stock_code(self, stock_code):
        if stock_code is not None:
            self.stock_code = stock_code

    def get_date(self):
        return self.date

    def set_date(self, date):
        if date is not None:
            self.date = date

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

    def get_total_share(self):
        return self.total_share

    def set_total_share(self, total_share):
        if total_share is not None:
            self.total_share = total_share

    def get_total_current_assets(self):
        return self.total_current_assets

    def set_total_current_assets(self, total_current_assets):
        if total_current_assets is not None:
            self.total_current_assets = total_current_assets

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

    def get_main_business_income(self):
        return self.main_business_income

    def set_main_business_income(self, main_business_income):
        if main_business_income is not None:
            self.main_business_income = main_business_income

    def get_financial_expenses(self):
        return self.financial_expenses

    def set_financial_expenses(self, financial_expenses):
        if financial_expenses is not None:
            self.financial_expenses = financial_expenses

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

    def to_tuple(self, include_id=False):
        if include_id:
            result = tuple((self.id, self.stock_code, self.date,
                            self.book_value_per_share, self.cash_flow_per_share,
                            self.total_share, self.total_current_assets, self.total_assets,
                            self.total_long_term_liabilities,
                            self.debt_to_net_assets_ratio, self.main_business_income, self.financial_expenses,
                            self.net_profit, self.net_profit_per_share, self.net_profit_per_share_in_year,
                            self.rate, self.roi, self.roe, self.pe, self.pb,
                            self.dividend, self.dividend_yield, self.dividend_ratio,
                            self.created, self.modified))
        else:
            result = tuple((self.stock_code, self.date,
                            self.book_value_per_share, self.cash_flow_per_share,
                            self.total_share, self.total_current_assets, self.total_assets,
                            self.total_long_term_liabilities,
                            self.debt_to_net_assets_ratio, self.main_business_income, self.financial_expenses,
                            self.net_profit, self.net_profit_per_share, self.net_profit_per_share_in_year,
                            self.rate, self.roi, self.roe, self.pe, self.pb,
                            self.dividend, self.dividend_yield, self.dividend_ratio,
                            self.created, self.modified))
        return result

    def setup_net_profit_per_share(self):
        if self.total_share == 0:
            return

        self.net_profit_per_share = round(self.net_profit / self.total_share, Constants.DOUBLE_FIXED_DECIMAL)

    def setup_debt_to_net_assets_ratio(self):
        if self.total_share == 0:
            return

        if self.book_value_per_share == 0:
            return

        self.debt_to_net_assets_ratio = self.total_long_term_liabilities / self.total_share / self.book_value_per_share

    @staticmethod
    def get_delete_sql():
        delete_sql = "DELETE FROM financial_data WHERE stock_code = ?"
        return delete_sql

    @staticmethod
    def get_insert_sql():
        insert_sql = "INSERT INTO financial_data (stock_code, date," \
                     "book_value_per_share, cash_flow_per_share," \
                     "total_share, total_current_assets, total_assets, total_long_term_liabilities," \
                     "debt_to_net_assets_ratio, main_business_income, financial_expenses," \
                     "net_profit, net_profit_per_share, net_profit_per_share_in_year," \
                     "rate, roi, roe, pe, pb," \
                     "dividend, dividend_yield, dividend_ratio," \
                     "created, modified)" \
                     " VALUES(?,?," \
                     "?,?," \
                     "?,?,?,?," \
                     "?,?,?," \
                     "?,?,?," \
                     "?,?,?,?,?," \
                     "?,?,?," \
                     "?,?)"
        return insert_sql
