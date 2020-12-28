# -*- coding: utf-8 -*-
import DatabaseContract


class TotalShare:
    def __init__(self, total_share_tuple=None):
        self.id = 0
        self.stock_code = ""
        self.date = ""
        self.total_share = ""
        self.created = ""
        self.modified = ""

        if total_share_tuple is None:
            return

        self.set_id(total_share_tuple[0])
        self.set_stock_code(total_share_tuple[DatabaseContract.TotalShareColumn.stock_code.value])
        self.set_date(total_share_tuple[DatabaseContract.TotalShareColumn.date.value])
        self.set_total_share(total_share_tuple[DatabaseContract.TotalShareColumn.total_share.value])
        self.set_created(total_share_tuple[DatabaseContract.TotalShareColumn.created.value])
        self.set_modified(total_share_tuple[DatabaseContract.TotalShareColumn.modified.value])

    def set_id(self, id):
        if id is not None:
            self.id = id

    def set_stock_code(self, stock_code):
        if stock_code is not None:
            self.stock_code = stock_code

    def set_date(self, date):
        if date is not None:
            self.date = date

    def set_total_share(self, total_share):
        if total_share is not None:
            self.total_share = total_share

    def set_created(self, created):
        if created is not None:
            self.created = created

    def set_modified(self, modified):
        if modified is not None:
            self.modified = modified