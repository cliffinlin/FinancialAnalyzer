# -*- coding: utf-8 -*-

from enum import Enum, auto


class SettingColumn(Enum):
    id = 0
    key = auto()
    value = auto()
    created = auto()
    modified = auto()


SQL_CREATE_TABLE_SETTING = " CREATE TABLE IF NOT EXISTS setting ( " \
                           + SettingColumn.id.name + " INTEGER PRIMARY KEY AUTOINCREMENT," \
                           + SettingColumn.key.name + " TEXT NOT NULL," \
                           + SettingColumn.value.name + " TEXT NOT NULL," \
                           + SettingColumn.created.name + " TEXT," \
                           + SettingColumn.modified.name + " TEXT" \
                           + "); "


class StockColumn(Enum):
    id = 0
    classes = auto()
    se = auto()
    code = auto()
    name = auto()
    pinyin = auto()
    flag = auto()
    price = auto()
    change = auto()
    net = auto()
    volume = auto()
    value = auto()

    date = auto()
    time = auto()
    min5 = auto()
    min15 = auto()
    min30 = auto()
    min60 = auto()
    day = auto()
    week = auto()
    month = auto()

    operation = auto()
    hold = auto()
    cost = auto()
    profit = auto()
    bonus = auto()
    valuation = auto()

    market_value = auto()

    total_share = auto()
    total_assets = auto()
    total_long_term_liabilities = auto()

    debt_to_net_assets_ratio = auto()

    main_business_income = auto()
    main_business_income_in_year = auto()

    book_value_per_share = auto()
    cash_flow_per_share = auto()

    net_profit = auto()
    net_profit_in_year = auto()
    net_profit_per_share = auto()
    net_profit_per_share_in_year = auto()
    net_profit_per_share_last_year = auto() #TODO remove
    net_profit_margin = auto()

    rate = auto()
    roi = auto()
    roe = auto()
    pe = auto()
    pb = auto()

    dividend = auto()
    dividend_yield = auto()
    dividend_ratio = auto()
    r_date = auto()

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
                         + StockColumn.flag.name + " INTEGER," \
                         + StockColumn.price.name + " DOUBLE," \
                         + StockColumn.change.name + " DOUBLE," \
                         + StockColumn.net.name + " DOUBLE," \
                         + StockColumn.volume.name + " DOUBLE," \
                         + StockColumn.value.name + " DOUBLE," \
                         + StockColumn.date.name + " TEXT," \
                         + StockColumn.time.name + " TEXT," \
                         + StockColumn.min5.name + " TEXT," \
                         + StockColumn.min15.name + " TEXT," \
                         + StockColumn.min30.name + " TEXT," \
                         + StockColumn.min60.name + " TEXT," \
                         + StockColumn.day.name + " TEXT," \
                         + StockColumn.week.name + " TEXT," \
                         + StockColumn.month.name + " TEXT," \
                         + StockColumn.operation.name + " INTEGER," \
                         + StockColumn.hold.name + " INTEGER," \
                         + StockColumn.cost.name + " DOUBLE," \
                         + StockColumn.profit.name + " DOUBLE," \
                         + StockColumn.bonus.name + " DOUBLE," \
                         + StockColumn.valuation.name + " DOUBLE," \
                         + StockColumn.market_value.name + " DOUBLE," \
                         + StockColumn.total_share.name + " DOUBLE," \
                         + StockColumn.total_assets.name + " DOUBLE," \
                         + StockColumn.total_long_term_liabilities.name + " DOUBLE," \
                         + StockColumn.debt_to_net_assets_ratio.name + " DOUBLE," \
                         + StockColumn.main_business_income.name + " DOUBLE," \
                         + StockColumn.main_business_income_in_year.name + " DOUBLE," \
                         + StockColumn.book_value_per_share.name + " DOUBLE," \
                         + StockColumn.cash_flow_per_share.name + " DOUBLE," \
                         + StockColumn.net_profit.name + " DOUBLE," \
                         + StockColumn.net_profit_in_year.name + " DOUBLE," \
                         + StockColumn.net_profit_per_share.name + " DOUBLE," \
                         + StockColumn.net_profit_per_share_in_year.name + " DOUBLE," \
                         + StockColumn.net_profit_per_share_last_year.name + " DOUBLE," \
                         + StockColumn.net_profit_margin.name + " DOUBLE," \
                         + StockColumn.rate.name + " DOUBLE," \
                         + StockColumn.roi.name + " DOUBLE," \
                         + StockColumn.roe.name + " DOUBLE," \
                         + StockColumn.pe.name + " DOUBLE," \
                         + StockColumn.pb.name + " DOUBLE," \
                         + StockColumn.dividend.name + " DOUBLE," \
                         + StockColumn.dividend_yield.name + " DOUBLE," \
                         + StockColumn.dividend_ratio.name + " DOUBLE," \
                         + StockColumn.r_date.name + " TEXT," \
                         + StockColumn.time_to_market.name + " TEXT," \
                         + StockColumn.created.name + " TEXT," \
                         + StockColumn.modified.name + " TEXT" \
                         + "); "


class StockDataColumn(Enum):
    id = 0
    stock_id = auto()
    date = auto()
    time = auto()
    period = auto()
    open = auto()
    high = auto()
    low = auto()
    close = auto()
    amplitude = auto()
    vertex_high = auto()
    vertex_low = auto()
    overlap = auto()
    overlap_high = auto()
    overlap_low = auto()
    average5 = auto()
    average10 = auto()
    dif = auto()
    dea = auto()
    histogram = auto()
    sigma_histogram = auto()
    roi = auto()
    pe = auto()
    pb = auto()
    dividend_yield = auto()
    level = auto()
    direction = auto()
    vertex = auto()
    divergence = auto()
    action = auto()
    created = auto()
    modified = auto()


SQL_CREATE_TABLE_STOCK_DATA = " CREATE TABLE IF NOT EXISTS stock_data ( " \
                              + StockDataColumn.id.name + " INTEGER PRIMARY KEY AUTOINCREMENT," \
                              + StockDataColumn.stock_id.name + " TEXT NOT NULL," \
                              + StockDataColumn.date.name + " TEXT NOT NULL," \
                              + StockDataColumn.time.name + " TEXT NOT NULL," \
                              + StockDataColumn.period.name + " TEXT NOT NULL," \
                              + StockDataColumn.open.name + " DOUBLE," \
                              + StockDataColumn.high.name + " DOUBLE," \
                              + StockDataColumn.low.name + " DOUBLE," \
                              + StockDataColumn.close.name + " DOUBLE," \
                              + StockDataColumn.amplitude.name + " DOUBLE," \
                              + StockDataColumn.vertex_high.name + " DOUBLE," \
                              + StockDataColumn.vertex_low.name + " DOUBLE," \
                              + StockDataColumn.overlap.name + " DOUBLE," \
                              + StockDataColumn.overlap_high.name + " DOUBLE," \
                              + StockDataColumn.overlap_low.name + " DOUBLE," \
                              + StockDataColumn.average5.name + " DOUBLE," \
                              + StockDataColumn.average10.name + " DOUBLE," \
                              + StockDataColumn.dif.name + " DOUBLE," \
                              + StockDataColumn.dea.name + " DOUBLE," \
                              + StockDataColumn.histogram.name + " DOUBLE," \
                              + StockDataColumn.sigma_histogram.name + " DOUBLE," \
                              + StockDataColumn.roi.name + " DOUBLE," \
                              + StockDataColumn.pe.name + " DOUBLE," \
                              + StockDataColumn.pb.name + " DOUBLE," \
                              + StockDataColumn.dividend_yield.name + " DOUBLE," \
                              + StockDataColumn.level.name + " INTEGER," \
                              + StockDataColumn.direction.name + " INTEGER," \
                              + StockDataColumn.vertex.name + " INTEGER," \
                              + StockDataColumn.divergence.name + " INTEGER," \
                              + StockDataColumn.action.name + " TEXT," \
                              + StockDataColumn.created.name + " TEXT," \
                              + StockDataColumn.modified.name + " TEXT" \
                              + "); "


class StockFinancialColumn(Enum):
    id = 0
    stock_id = auto()
    date = auto()
    book_value_per_share = auto()
    cash_flow_per_share = auto()
    total_share = auto()
    total_current_assets = auto()
    total_assets = auto()
    total_long_term_liabilities = auto()
    debt_to_net_assets_ratio = auto()
    main_business_income = auto()
    financial_expenses = auto()
    net_profit = auto()
    net_profit_per_share = auto()
    net_profit_per_share_in_year = auto()
    rate = auto()
    roi = auto()
    roe = auto()
    pe = auto()
    pb = auto()
    dividend = auto()
    dividend_yield = auto()
    dividend_ratio = auto()
    created = auto()
    modified = auto()


SQL_CREATE_TABLE_STOCK_FINANCIAL = " CREATE TABLE IF NOT EXISTS stock_financial ( " \
                                   + StockFinancialColumn.id.name + " INTEGER PRIMARY KEY AUTOINCREMENT," \
                                   + StockFinancialColumn.stock_id.name + " TEXT NOT NULL," \
                                   + StockFinancialColumn.date.name + " TEXT NOT NULL," \
                                   + StockFinancialColumn.book_value_per_share.name + " DOUBLE," \
                                   + StockFinancialColumn.cash_flow_per_share.name + " DOUBLE," \
                                   + StockFinancialColumn.total_share.name + " DOUBLE," \
                                   + StockFinancialColumn.total_current_assets.name + " DOUBLE," \
                                   + StockFinancialColumn.total_assets.name + " DOUBLE," \
                                   + StockFinancialColumn.total_long_term_liabilities.name + " DOUBLE," \
                                   + StockFinancialColumn.debt_to_net_assets_ratio.name + " DOUBLE," \
                                   + StockFinancialColumn.main_business_income.name + " DOUBLE," \
                                   + StockFinancialColumn.financial_expenses.name + " DOUBLE," \
                                   + StockFinancialColumn.net_profit.name + " DOUBLE," \
                                   + StockFinancialColumn.net_profit_per_share.name + " DOUBLE," \
                                   + StockFinancialColumn.net_profit_per_share_in_year.name + " DOUBLE," \
                                   + StockFinancialColumn.rate.name + " DOUBLE," \
                                   + StockFinancialColumn.roi.name + " DOUBLE," \
                                   + StockFinancialColumn.roe.name + " DOUBLE," \
                                   + StockFinancialColumn.pe.name + " DOUBLE," \
                                   + StockFinancialColumn.pb.name + " DOUBLE," \
                                   + StockFinancialColumn.dividend.name + " DOUBLE," \
                                   + StockFinancialColumn.dividend_yield.name + " DOUBLE," \
                                   + StockFinancialColumn.dividend_ratio.name + " DOUBLE," \
                                   + StockFinancialColumn.created.name + " TEXT," \
                                   + StockFinancialColumn.modified.name + " TEXT" \
                                   + "); "


class ShareBonusColumn(Enum):
    id = 0
    stock_id = auto()
    date = auto()
    dividend = auto()
    r_date = auto()
    created = auto()
    modified = auto()


SQL_CREATE_TABLE_SHARE_BONUS = " CREATE TABLE IF NOT EXISTS share_bonus ( " \
                               + ShareBonusColumn.id.name + " INTEGER PRIMARY KEY AUTOINCREMENT," \
                               + ShareBonusColumn.stock_id.name + " TEXT NOT NULL," \
                               + ShareBonusColumn.date.name + " TEXT NOT NULL," \
                               + ShareBonusColumn.dividend.name + " TEXT NOT NULL," \
                               + ShareBonusColumn.r_date.name + " TEXT NOT NULL," \
                               + ShareBonusColumn.created.name + " TEXT," \
                               + ShareBonusColumn.modified.name + " TEXT" \
                               + "); "


class TotalShareColumn(Enum):
    id = 0
    stock_id = auto()
    date = auto()
    total_share = auto()
    created = auto()
    modified = auto()


SQL_CREATE_TABLE_TOTAL_SHARE = " CREATE TABLE IF NOT EXISTS total_share ( " \
                               + TotalShareColumn.id.name + " INTEGER PRIMARY KEY AUTOINCREMENT," \
                               + TotalShareColumn.stock_id.name + " TEXT NOT NULL," \
                               + TotalShareColumn.date.name + " TEXT NOT NULL," \
                               + TotalShareColumn.total_share.name + " DOUBLE," \
                               + TotalShareColumn.created.name + " TEXT," \
                               + TotalShareColumn.modified.name + " TEXT" \
                               + "); "
