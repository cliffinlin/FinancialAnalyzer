# -*- coding: utf-8 -*-
import DatabaseContract
from DatabaseTable import DatabaseTable


class TotalShare(DatabaseTable):
    def __init__(self, total_share_tuple=None):
        DatabaseTable.__init__(self)

        self.stock_code = ""
        self.date = ""
        self.total_share = ""

        self.set(total_share_tuple)

    def set(self, total_share_tuple):
        if total_share_tuple is None:
            return

        DatabaseTable.set(self,
                          total_share_tuple[DatabaseContract.TotalShareColumn.id.value],
                          total_share_tuple[DatabaseContract.TotalShareColumn.created.value],
                          total_share_tuple[DatabaseContract.TotalShareColumn.modified.value])

        self.set_stock_code(total_share_tuple[DatabaseContract.TotalShareColumn.stock_code.value])
        self.set_date(total_share_tuple[DatabaseContract.TotalShareColumn.date.value])
        self.set_total_share(total_share_tuple[DatabaseContract.TotalShareColumn.total_share.value])

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

    def get_total_share(self):
        return self.total_share

    def set_total_share(self, total_share):
        if total_share is not None:
            self.total_share = total_share

    def to_tuple(self, include_id=False):
        if include_id:
            result = tuple((self.id, self.stock_code, self.date,
                            self.total_share,
                            self.created, self.modified))
        else:
            result = tuple((self.stock_code, self.date,
                            self.total_share,
                            self.created, self.modified))
        return result

    @staticmethod
    def get_delete_sql():
        delete_sql = "DELETE FROM total_share WHERE stock_code = ?"
        return delete_sql

    @staticmethod
    def get_insert_sql():
        insert_sql = "INSERT INTO total_share (stock_code, date," \
                     "total_share," \
                     "created, modified)" \
                     " VALUES(?,?," \
                     "?," \
                     "?,?)"
        return insert_sql
