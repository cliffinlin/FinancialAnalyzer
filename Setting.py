# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime, date

import Constants
import DatabaseContract
import Utility
from DatabaseTable import DatabaseTable


class Setting(DatabaseTable):
    def __init__(self, setting_tuple=None):
        DatabaseTable.__init__(self)

        self.key = ""
        self.value = ""

        self.set(setting_tuple)

    def set(self, setting_tuple):
        if setting_tuple is None:
            return

        self.set_id(setting_tuple[DatabaseContract.SettingColumn.id.value])
        self.set_key(setting_tuple[DatabaseContract.SettingColumn.key.value])
        self.set_value(setting_tuple[DatabaseContract.SettingColumn.value.value])
        self.set_created(setting_tuple[DatabaseContract.SettingColumn.created.value])
        self.set_modified(setting_tuple[DatabaseContract.SettingColumn.modified.value])

    def get_key(self):
        return self.key

    def set_key(self, key):
        if key is not None:
            self.key = key

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value is not None:
            self.value = value

    def to_tuple(self, include_id=False):
        if include_id:
            result = tuple((self.id, self.key, self.value,
                            self.created, self.modified))
        else:
            result = tuple((self.key, self.value,
                            self.created, self.modified))
        return result

    def get_insert_tuple(self):
        return tuple((self.key, self.value,
                      self.created, self.modified))

    def get_update_tuple(self):
        return tuple((self.value,
                      self.modified, self.key))

    @staticmethod
    def get_delete_sql():
        sql = "DELETE FROM setting WHERE key=?"
        return sql

    @staticmethod
    def get_insert_sql():
        sql = "INSERT INTO setting (key, value," \
              "created, modified)" \
              " VALUES(?,?," \
              "?,?)"
        return sql

    @staticmethod
    def get_update_sql():
        sql = "UPDATE setting SET " \
              "value=?," \
              "modified=? " \
              " WHERE " \
              "key=?"
        return sql

    @staticmethod
    def read_from_database(key):
        if key is None:
            return None

        return Utility.fetchone_from_database("SELECT * FROM setting WHERE key = ? ", (key,))

    @staticmethod
    def write_to_database(key, value):
        connect = None

        if key is None:
            print("key is None, return")
            return

        try:
            connect = sqlite3.connect(Constants.DATA_DATABASE_ORION_DB)
            cursor = connect.cursor()

            setting_obj = Setting()
            setting_obj.set_key(key)
            setting_obj.set_value(value)

            now = datetime.now().strftime(Constants.DATE_TIME_FORMAT)

            setting_tuple = Setting.read_from_database(key)

            if setting_tuple is None:
                setting_obj.set_created(now)
                setting_obj.set_modified(now)
                cursor.execute(Setting.get_insert_sql(), setting_obj.get_insert_tuple())
            else:
                setting_obj.set_modified(now)
                cursor.execute(Setting.get_update_sql(), setting_obj.get_update_tuple())

            connect.commit()
        except sqlite3.Error as e:
            print('e:', e)
        finally:
            if connect is not None:
                connect.close()

    @staticmethod
    def need_download_stock_list():
        setting_tuple = Setting.read_from_database(Constants.SETTING_KEY_DOWNLOAD_STOCK_LIST)
        if Utility.is_empty(setting_tuple):
            return True

        setting = Setting(setting_tuple)
        if Utility.is_empty(setting.get_value()):
            return True

        today_string = datetime.strftime(date.today(), '%Y-%m-%d')
        if today_string not in setting.get_modified():
            return True

        return False
