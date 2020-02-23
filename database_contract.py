# -*- coding: utf-8 -*-

from enum import Enum, auto

DATABASE_FILE_NAME = "orion.db"


class StockColumn(Enum):
    id = 0
    classes = auto()
    se = auto()
    code = auto()
    name = auto()
    pinyin = auto()
    mark = auto()
    price = auto()
    change = auto()
    net = auto()
    volume = auto()
    value = auto()
    operation = auto()
    hold = auto()
    cost = auto()
    profit = auto()
    total_share = auto()
    roe = auto()
    rate = auto()
    valuation = auto()
    discount = auto()
    pe = auto()
    pb = auto()
    dividend = auto()
    dividend_yield = auto()
    delta = auto()
    time_to_market = auto()
    created = auto()
    modified = auto()


SQL_CREATE_TABLE_STOCK = " CREATE TABLE IF NOT EXISTS stock ( " \
                         + StockColumn.id.name + " INTEGER PRIMARY KEY AUTOINCREMENT," \
                         + StockColumn.classes.name + " TEXT," \
                         + StockColumn.se.name + " TEXT NOT NULL," \
                         + StockColumn.code.name + " TEXT NOT NULL," \
                         + StockColumn.name.name + " TEXT NOT NULL," \
                         + StockColumn.pinyin.name + " TEXT," \
                         + StockColumn.mark.name + " INTEGER," \
                         + StockColumn.price.name + " DOUBLE," \
                         + StockColumn.change.name + " DOUBLE," \
                         + StockColumn.net.name + " DOUBLE," \
                         + StockColumn.volume.name + " DOUBLE," \
                         + StockColumn.value.name + " DOUBLE," \
                         + StockColumn.operation.name + " INTEGER," \
                         + StockColumn.hold.name + " INTEGER," \
                         + StockColumn.cost.name + " DOUBLE," \
                         + StockColumn.profit.name + " DOUBLE," \
                         + StockColumn.total_share.name + " DOUBLE," \
                         + StockColumn.roe.name + " DOUBLE," \
                         + StockColumn.rate.name + " DOUBLE," \
                         + StockColumn.valuation.name + " DOUBLE," \
                         + StockColumn.discount.name + " DOUBLE," \
                         + StockColumn.pe.name + " DOUBLE," \
                         + StockColumn.pb.name + " DOUBLE," \
                         + StockColumn.dividend.name + " DOUBLE," \
                         + StockColumn.dividend_yield.name + " DOUBLE," \
                         + StockColumn.delta.name + " DOUBLE," \
                         + StockColumn.time_to_market.name + " TEXT," \
                         + StockColumn.created.name + " TEXT," \
                         + StockColumn.modified.name + " TEXT" \
                         + "); "


class StockDataColumn(Enum):
    id = 0
    stock_code = auto()
    date = auto()
    time = auto()
    period = auto()
    open = auto()
    high = auto()
    low = auto()
    close = auto()
    volume = auto()
    value = auto()
    created = auto()
    modified = auto()


SQL_CREATE_TABLE_STOCK_DATA = " CREATE TABLE IF NOT EXISTS stock_data ( " \
                              + StockDataColumn.id.name + " INTEGER PRIMARY KEY AUTOINCREMENT," \
                              + StockDataColumn.stock_code.name + " TEXT NOT NULL," \
                              + StockDataColumn.date.name + " TEXT NOT NULL," \
                              + StockDataColumn.time.name + " TEXT NOT NULL," \
                              + StockDataColumn.period.name + " TEXT NOT NULL," \
                              + StockDataColumn.open.name + " DOUBLE," \
                              + StockDataColumn.high.name + " DOUBLE," \
                              + StockDataColumn.low.name + " DOUBLE," \
                              + StockDataColumn.close.name + " DOUBLE," \
                              + StockDataColumn.volume.name + " DOUBLE," \
                              + StockDataColumn.value.name + " DOUBLE," \
                              + StockDataColumn.created.name + " TEXT," \
                              + StockDataColumn.modified.name + " TEXT" \
                              + "); "


class FinancialDataColumn(Enum):
    id = 0
    stock_code = auto()
    date = auto()
    book_value_per_share = auto()
    cash_flow_per_share = auto()
    total_current_assets = auto()
    total_assets = auto()
    total_long_term_liabilities = auto()
    main_business_income = auto()
    financial_expenses = auto()
    net_profit = auto()
    net_profit_per_share = auto()
    created = auto()
    modified = auto()


SQL_CREATE_TABLE_FINANCIAL_DATA = " CREATE TABLE IF NOT EXISTS financial_data ( " \
                                  + FinancialDataColumn.id.name + " INTEGER PRIMARY KEY AUTOINCREMENT," \
                                  + FinancialDataColumn.stock_code.name + " TEXT NOT NULL," \
                                  + FinancialDataColumn.date.name + " TEXT NOT NULL," \
                                  + FinancialDataColumn.book_value_per_share.name + " TEXT NOT NULL," \
                                  + FinancialDataColumn.cash_flow_per_share.name + " DOUBLE," \
                                  + FinancialDataColumn.total_current_assets.name + " DOUBLE," \
                                  + FinancialDataColumn.total_assets.name + " DOUBLE," \
                                  + FinancialDataColumn.total_long_term_liabilities.name + " DOUBLE," \
                                  + FinancialDataColumn.main_business_income.name + " DOUBLE," \
                                  + FinancialDataColumn.financial_expenses.name + " DOUBLE," \
                                  + FinancialDataColumn.net_profit.name + " DOUBLE," \
                                  + FinancialDataColumn.net_profit_per_share.name + " DOUBLE," \
                                  + FinancialDataColumn.created.name + " TEXT," \
                                  + FinancialDataColumn.modified.name + " TEXT" \
                                  + "); "


class ShareBonusColumn(Enum):
    id = 0
    stock_code = auto()
    date = auto()
    dividend = auto()
    dividend_date = auto()
    created = auto()
    modified = auto()


SQL_CREATE_TABLE_SHARE_BONUS = " CREATE TABLE IF NOT EXISTS share_bonus ( " \
                               + ShareBonusColumn.id.name + " INTEGER PRIMARY KEY AUTOINCREMENT," \
                               + ShareBonusColumn.stock_code.name + " TEXT NOT NULL," \
                               + ShareBonusColumn.date.name + " TEXT NOT NULL," \
                               + ShareBonusColumn.dividend.name + " TEXT NOT NULL," \
                               + ShareBonusColumn.dividend_date.name + " TEXT NOT NULL," \
                               + ShareBonusColumn.created.name + " TEXT," \
                               + ShareBonusColumn.modified.name + " TEXT" \
                               + "); "
