import sqlite3

import Constants
import DatabaseContract
import Utility
from configparser import ConfigParser


def make_data_directory():
    print(make_data_directory.__name__)

    Utility.makedir(Constants.DATA_PATH)
    Utility.makedir(Constants.DATA_DATABASE_PATH)
    Utility.makedir(Constants.DATA_FIGURE_PATH)
    Utility.makedir(Constants.DATA_FINANCIAL_PATH)
    Utility.makedir(Constants.DATA_SHARE_BONUS_PATH)
    Utility.makedir(Constants.DATA_TOTAL_SHARE_PATH)
    Utility.makedir(Constants.DATA_STOCK_PATH)
    Utility.makedir(Constants.DATA_STOCK_DAY_PATH)
    Utility.makedir(Constants.DATA_STOCK_WEEK_PATH)
    Utility.makedir(Constants.DATA_STOCK_MONTH_PATH)


def setup_database():
    print(setup_database.__name__)

    connect = None

    try:
        connect = sqlite3.connect(Constants.DATA_DATABASE_ORION_DB)
        if connect is None:
            return

        cursor = connect.cursor()
        if cursor is None:
            return

        cursor.execute(DatabaseContract.SQL_CREATE_TABLE_STOCK)
        cursor.execute(DatabaseContract.SQL_CREATE_TABLE_STOCK_DATA)
        cursor.execute(DatabaseContract.SQL_CREATE_TABLE_FINANCIAL_DATA)
        cursor.execute(DatabaseContract.SQL_CREATE_TABLE_SHARE_BONUS)
        cursor.execute(DatabaseContract.SQL_CREATE_TABLE_TOTAL_SHARE)

        connect.commit()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()


def setup_config_ini():
    print(setup_config_ini.__name__)

    config = ConfigParser()
    config.read(Constants.CONFIG_INI_FILE_NAME)
    if not config.has_section(Constants.CONFIG_INI_DOWNLOAD):
        config.add_section(Constants.CONFIG_INI_DOWNLOAD)
        config.set(Constants.CONFIG_INI_DOWNLOAD, Constants.CONFIG_INI_INDEX, "0")
        with open(Constants.CONFIG_INI_FILE_NAME, 'w') as f:
            config.write(f)


def initialize():
    print(initialize.__name__)

    make_data_directory()
    setup_database()
    setup_config_ini()
