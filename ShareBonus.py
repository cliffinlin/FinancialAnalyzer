# -*- coding: utf-8 -*-
import DatabaseContract


class ShareBonus:
    def __init__(self, share_bonus_tuple=None):
        self.id = 0
        self.stock_code = ""
        self.date = ""
        self.dividend = ""
        self.dividend_date = ""
        self.created = ""
        self.modified = ""

        if share_bonus_tuple is None:
            return

        self.set_id(share_bonus_tuple[0])
        self.set_stock_code(share_bonus_tuple[DatabaseContract.ShareBonusColumn.stock_code.value])
        self.set_date(share_bonus_tuple[DatabaseContract.ShareBonusColumn.date.value])
        self.set_dividend(share_bonus_tuple[DatabaseContract.ShareBonusColumn.dividend.value])
        self.set_dividend_date(share_bonus_tuple[DatabaseContract.ShareBonusColumn.dividend_date.value])
        self.set_created(share_bonus_tuple[DatabaseContract.ShareBonusColumn.created.value])
        self.set_modified(share_bonus_tuple[DatabaseContract.ShareBonusColumn.modified.value])

    def set_id(self, id):
        if id is not None:
            self.id = id

    def set_stock_code(self, stock_code):
        if stock_code is not None:
            self.stock_code = stock_code

    def set_date(self, date):
        if date is not None:
            self.date = date

    def set_dividend(self, dividend):
        if dividend is not None:
            self.dividend = dividend

    def set_dividend_date(self, dividend_date):
        if dividend_date is not None:
            self.dividend_date = dividend_date

    def set_created(self, created):
        if created is not None:
            self.created = created

    def set_modified(self, modified):
        if modified is not None:
            self.modified = modified
