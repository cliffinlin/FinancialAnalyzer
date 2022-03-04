# -*- coding: utf-8 -*-
import DatabaseContract
from DatabaseTable import DatabaseTable


class ShareHolder(DatabaseTable):
    def __init__(self, share_holder_tuple=None):
        DatabaseTable.__init__(self)

        self.stock_code = ""
        self.date = ""
        self.type = ""
        self.number = 0
        self.hold = 0
        self.ratio = 0

        self.set(share_holder_tuple)

    def set(self, share_holder_tuple):
        if share_holder_tuple is None:
            return

        DatabaseTable.set(self, share_holder_tuple[DatabaseContract.ShareHolderColumn.id.value],
                          share_holder_tuple[DatabaseContract.ShareHolderColumn.created.value],
                          share_holder_tuple[DatabaseContract.ShareHolderColumn.modified.value])

        self.set_stock_code(share_holder_tuple[DatabaseContract.ShareHolderColumn.stock_id.value])
        self.set_date(share_holder_tuple[DatabaseContract.ShareHolderColumn.date.value])
        self.set_type(share_holder_tuple[DatabaseContract.ShareHolderColumn.type.value])
        self.set_number(share_holder_tuple[DatabaseContract.ShareHolderColumn.number.value])
        self.set_hold(share_holder_tuple[DatabaseContract.ShareHolderColumn.hold.value])
        self.set_ratio(share_holder_tuple[DatabaseContract.ShareHolderColumn.ratio.value])

    def get_stock_id(self):
        return self.stock_id

    def set_stock_id(self, stock_id):
        if stock_id is not None:
            self.stock_id = stock_id

    def get_date(self):
        return self.date

    def set_date(self, date):
        if date is not None:
            self.date = date

    def get_type(self):
        return self.type

    def set_type(self, type):
        if type is not None:
            self.type = type

    def get_number(self):
        return self.number

    def set_number(self, number):
        if number is not None:
            self.number = number

    def get_hold(self):
        return self.hold

    def set_hold(self, hold):
        if hold is not None:
            self.hold = hold

    def get_ratio(self):
        return self.ratio

    def set_ratio(self, ratio):
        if ratio is not None:
            self.ratio = ratio

    def to_tuple(self, include_id=False):
        if include_id:
            result = tuple((self.id, self.stock_id,
                            self.date, self.type, self.number, self.hold, self.ratio,
                            self.created, self.modified))
        else:
            result = tuple((self.stock_id,
                            self.date, self.type, self.number, self.hold, self.ratio,
                            self.created, self.modified))
        return result

    @staticmethod
    def get_delete_sql():
        delete_sql = "DELETE FROM share_holder WHERE stock_id = ?"
        return delete_sql

    @staticmethod
    def get_insert_sql():
        insert_sql = "INSERT INTO share_holder (stock_id," \
                     "date, type, number, hold, ratio," \
                     "created, modified)" \
                     " VALUES(?," \
                     "?,?,?,?,?," \
                     "?,?)"
        return insert_sql
