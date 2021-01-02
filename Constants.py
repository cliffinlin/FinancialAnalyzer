# -*- coding: utf-8 -*-

ROI_COEFFICIENT = (1.0 / 10.0)

SEASONS_IN_A_YEAR = 4
DOUBLE_FIXED_DECIMAL = 2
DOUBLE_CONSTANT_WAN = 10000

TIME_TO_MARKET_YEAR_MIN = 5

# Stock Type
STOCK_TYPE_BLACK = -1
STOCK_TYPE_NONE = 0
STOCK_TYPE_FAVORITE = 1
TIME_TO_MARKET_YEAR_MIN = 5

DATE_FORMAT = "%Y-%m-%d"
DATE_TIME_FORMAT = "%Y-%m-%d %H:%M"

DAY = "day"
WEEK = "week"
MONTH = "month"

CONFIG_INI_FILE_NAME = "config.ini"
CONFIG_INI_DOWNLOAD = "download"
CONFIG_INI_INDEX = "index"

ORION_DATABASE_FILE_NAME = "orion.db"
STOCK_LIST_XML_FILE_NAME = "stock_list.xml"
STOCK_LIST_CODE_FILE_NAME = "stock_list.code"

DATA_PATH = "./data/"
DATA_DATABASE_PATH = DATA_PATH + "database" + "/"
DATA_FIGURE_PATH = DATA_PATH + "figure" + "/"
DATA_FINANCIAL_PATH = DATA_PATH + "financial" + "/"
DATA_SHARE_BONUS_PATH = DATA_PATH + "share_bonus" + "/"
DATA_TOTAL_SHARE_PATH = DATA_PATH + "total_share" + "/"
DATA_STOCK_PATH = DATA_PATH + "stock" + "/"
DATA_STOCK_DAY_PATH = DATA_STOCK_PATH + DAY + "/"
DATA_STOCK_WEEK_PATH = DATA_STOCK_PATH + WEEK + "/"
DATA_STOCK_MONTH_PATH = DATA_STOCK_PATH + MONTH + "/"

DATA_DATABASE_ORION_DB = DATA_DATABASE_PATH + ORION_DATABASE_FILE_NAME
DATA_STOCK_LIST_XML = DATA_STOCK_PATH + STOCK_LIST_XML_FILE_NAME
DATA_STOCK_LIST_CODE = DATA_STOCK_PATH + STOCK_LIST_CODE_FILE_NAME
