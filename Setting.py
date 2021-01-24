# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime

import Constants
import DatabaseContract
import Utility


class Setting:
    def __init__(self, setting_tuple=None):
        self.id = 0
        self.key = ""
        self.value = ""
        self.created = ""
        self.modified = ""

        if setting_tuple is None:
            return

        self.set_id(setting_tuple[0])
        self.set_key(setting_tuple[DatabaseContract.TotalShareColumn.key.value])
        self.set_value(setting_tuple[DatabaseContract.TotalShareColumn.value.value])
        self.set_created(setting_tuple[DatabaseContract.TotalShareColumn.created.value])
        self.set_modified(setting_tuple[DatabaseContract.TotalShareColumn.modified.value])

    def get_id(self):
        return self.id

    def set_id(self, id):
        if id is not None:
            self.id = id

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
    def read_setting_from_database(key):
        if key is None:
            return None

        return Utility.get_tuple_list_from_database("SELECT * FROM setting WHERE key = ? ", (key,))

    @staticmethod
    def write_setting_to_database(key, value):
        connect = None

        if key is None or value is None:
            print("key or value is empty, return")
            return

        try:
            connect = sqlite3.connect(Constants.DATA_DATABASE_ORION_DB)
            cursor = connect.cursor()

            setting_obj = Setting()
            setting_obj.set_key(key)
            setting_obj.set_value(value)

            now = datetime.now().strftime(Constants.DATE_TIME_FORMAT)

            if Setting.read_setting_from_database(key) is None:
                setting_obj.set_created(now)
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