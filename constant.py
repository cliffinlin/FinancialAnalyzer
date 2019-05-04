# -*- coding: utf-8 -*-

# Rating Type:
POOR_TYPE = -1
PRICE_TYPE = 1 << 0
LIABILITIES_TYPE = 1 << 1
GROWTH_TYPE = 1 << 2

# Analyze period:
GROWTH_YEAR_MIN = 3
TIME_TO_MARKET_YEAR_MIN = 5

# Checkout threshold
BOOK_VALUE_PER_SHARE_MIN = 1

PE_MAX = 20
PB_MAX = 2
ROE_MAX = 30

SEASONS_IN_A_YEAR = 4

DATE_FORMAT = "%Y-%m-%d"
DATE_TIME_FORMAT = "%Y-%m-%d %H:%M"

DAY = "day"
WEEK = "week"
MONTH = "month"

DATA_PATH = "./data/"
DATA_FINANCIAL_PATH = DATA_PATH + "financial" + "/"
DATA_STOCK_PATH = DATA_PATH + "stock" + "/"
DATA_STOCK_DAY_PATH = DATA_STOCK_PATH + DAY + "/"
DATA_STOCK_WEEK_PATH = DATA_STOCK_PATH + WEEK + "/"
DATA_STOCK_MONTH_PATH = DATA_STOCK_PATH + MONTH + "/"

DATABASE_NAME = "database.db"

SQL_SETUP_TABLE_STOCK = """ CREATE TABLE IF NOT EXISTS stock (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    code TEXT NOT NULL,
                                    name TEXT NOT NULL,
                                    industry TEXT,
                                    area TEXT,
                                    pe DOUBLE,
                                    outstanding DOUBLE,
                                    totals DOUBLE,
                                    total_assets DOUBLE,
                                    liquid_assets DOUBLE,
                                    fixed_assets DOUBLE,                   
                                    reserved DOUBLE,
                                    rps DOUBLE,
                                    eps DOUBLE,
                                    bvps DOUBLE,
                                    pb DOUBLE,
                                    time_to_market TEXT,
                                    undp DOUBLE,
                                    perundp DOUBLE,
                                    rev DOUBLE,
                                    profit DOUBLE,
                                    gpr DOUBLE,
                                    npr DOUBLE,
                                    holders DOUBLE,
                                    bvpsr DOUBLE,
                                    frechet DOUBLE,
                                    rating INTEGER,
                                    favorite INTEGER,
                                    created TEXT,
                                    modified TEXT
                                ); """

SQL_SETUP_TABLE_STOCK_DATA = """ CREATE TABLE IF NOT EXISTS stock_data (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    stock_code TEXT NOT NULL,
                                    date TEXT NOT NULL,
                                    time TEXT NOT NULL,
                                    period TEXT NOT NULL,
                                    open DOUBLE,
                                    high DOUBLE,
                                    low DOUBLE,
                                    close DOUBLE,
                                    volume DOUBLE,
                                    created TEXT,
                                    modified TEXT
                                ); """

SQL_SETUP_TABLE_FINANCIAL_DATA = """ CREATE TABLE IF NOT EXISTS financial_data (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    stock_code TEXT NOT NULL,
                                    date TEXT NOT NULL,
                                    book_value_per_share DOUBLE,
                                    earnings_per_share DOUBLE,
                                    cash_flow_per_share DOUBLE,
                                    total_current_assets DOUBLE,
                                    total_assets DOUBLE,
                                    total_long_term_liabilities DOUBLE,
                                    main_business_income DOUBLE,
                                    financial_expenses DOUBLE,
                                    net_profit DOUBLE,
                                    roe DOUBLE,
                                    book_value_per_share_rate DOUBLE,
                                    created TEXT,
                                    modified TEXT
                                ); """
