# -*- coding: utf-8 -*-
import os
import sqlite3
from configparser import ConfigParser
import Constants


def makedir(directory):
    if not os.path.exists(directory):
        print("makedir " + directory)
        os.makedirs(directory)


def is_empty(obj):
    if obj is None or len(obj) == 0:
        return True
    return False


def get_tuple_list_from_database(sql, parameters=None):
    connect = None
    tuple_list = tuple()

    if is_empty(sql):
        return None

    try:
        connect = sqlite3.connect(Constants.DATA_DATABASE_ORION_DB)
        if connect is None:
            return None

        cursor = connect.cursor()
        if cursor is None:
            return None

        cursor.execute(sql, parameters)
        tuple_list = cursor.fetchall()
    except sqlite3.Error as e:
        print('e:', e)
    finally:
        if connect is not None:
            connect.close()

    return tuple_list


def read_download_index_from_config_ini():
    config = ConfigParser()
    config.read(Constants.CONFIG_INI_FILE_NAME)

    return int(config.get(Constants.CONFIG_INI_DOWNLOAD, Constants.CONFIG_INI_INDEX))


def write_download_index_to_config_ini(index):
    config = ConfigParser()
    config.read(Constants.CONFIG_INI_FILE_NAME)

    config.set(Constants.CONFIG_INI_DOWNLOAD, Constants.CONFIG_INI_INDEX, str(index))
    with open(Constants.CONFIG_INI_FILE_NAME, 'w') as f:
        config.write(f)
