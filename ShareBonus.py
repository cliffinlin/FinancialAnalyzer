# -*- coding: utf-8 -*-
import DatabaseContract
from DatabaseTable import DatabaseTable


class ShareBonus(DatabaseTable):
    def __init__(self, share_bonus_tuple=None):
        DatabaseTable.__init__(self)

        self.stock_code = ""
        self.date = ""
        self.dividend = ""
        self.r_date = ""

        self.set(share_bonus_tuple)

    def set(self, share_bonus_tuple):
        if share_bonus_tuple is None:
            return

        self.set_id(share_bonus_tuple[DatabaseContract.ShareBonusColumn.id.value])
        self.set_stock_code(share_bonus_tuple[DatabaseContract.ShareBonusColumn.stock_code.value])
        self.set_date(share_bonus_tuple[DatabaseContract.ShareBonusColumn.date.value])
        self.set_dividend(share_bonus_tuple[DatabaseContract.ShareBonusColumn.dividend.value])
        self.set_r_date(share_bonus_tuple[DatabaseContract.ShareBonusColumn.r_date.value])
        self.set_created(share_bonus_tuple[DatabaseContract.ShareBonusColumn.created.value])
        self.set_modified(share_bonus_tuple[DatabaseContract.ShareBonusColumn.modified.value])

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

    def get_dividend(self):
        return self.dividend

    def set_dividend(self, dividend):
        if dividend is not None:
            self.dividend = dividend

    def get_r_date(self):
        return self.r_date

    def set_r_date(self, r_date):
        if r_date is not None:
            self.r_date = r_date

    def to_tuple(self, include_id=False):
        if include_id:
            result = tuple((self.id, self.stock_code, self.date,
                            self.dividend, self.r_date,
                            self.created, self.modified))
        else:
            result = tuple((self.stock_code, self.date,
                            self.dividend, self.r_date,
                            self.created, self.modified))
        return result

    @staticmethod
    def get_delete_sql():
        delete_sql = "DELETE FROM share_bonus WHERE stock_code = ?"
        return delete_sql

    @staticmethod
    def get_insert_sql():
        insert_sql = "INSERT INTO share_bonus (stock_code, date, " \
                     "dividend, r_date, " \
                     "created, modified)" \
                     " VALUES(?,?," \
                     "?,?," \
                     "?,?)"
        return insert_sql
