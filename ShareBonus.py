# -*- coding: utf-8 -*-
import DatabaseContract


class ShareBonus:
    def __init__(self, share_bonus_tuple=None):
        self.id = 0
        self.stock_code = ""
        self.date = ""
        self.dividend = ""
        self.r_date = ""
        self.created = ""
        self.modified = ""

        if share_bonus_tuple is None:
            return

        self.set_id(share_bonus_tuple[0])
        self.set_stock_code(share_bonus_tuple[DatabaseContract.ShareBonusColumn.stock_code.value])
        self.set_date(share_bonus_tuple[DatabaseContract.ShareBonusColumn.date.value])
        self.set_dividend(share_bonus_tuple[DatabaseContract.ShareBonusColumn.dividend.value])
        self.set_r_date(share_bonus_tuple[DatabaseContract.ShareBonusColumn.r_date.value])
        self.set_created(share_bonus_tuple[DatabaseContract.ShareBonusColumn.created.value])
        self.set_modified(share_bonus_tuple[DatabaseContract.ShareBonusColumn.modified.value])

    def get_id(self):
        return self.id

    def set_id(self, id):
        if id is not None:
            self.id = id

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