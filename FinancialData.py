# -*- coding: utf-8 -*-
import DatabaseContract


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
        self.set_stock_code(financial_data_tuple[DatabaseContract.FinancialDataColumn.stock_code.value])
        self.set_date(financial_data_tuple[DatabaseContract.FinancialDataColumn.date.value])
        self.set_book_value_per_share(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.book_value_per_share.value])
        self.set_cash_flow_per_share(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.cash_flow_per_share.value])
        self.set_total_current_assets(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.total_current_assets.value])
        self.set_total_assets(financial_data_tuple[DatabaseContract.FinancialDataColumn.total_assets.value])
        self.set_total_long_term_liabilities(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.total_long_term_liabilities.value])
        self.set_main_business_income(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.main_business_income.value])
        self.set_financial_expenses(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.financial_expenses.value])
        self.set_net_profit(financial_data_tuple[DatabaseContract.FinancialDataColumn.net_profit.value])
        self.set_net_profit_per_share(
            financial_data_tuple[DatabaseContract.FinancialDataColumn.net_profit_per_share.value])
        self.set_created(financial_data_tuple[DatabaseContract.FinancialDataColumn.created.value])
        self.set_modified(financial_data_tuple[DatabaseContract.FinancialDataColumn.modified.value])

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
