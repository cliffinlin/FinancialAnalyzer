# -*- coding: utf-8 -*-
import DatabaseContract


class StockHolder:
    def __init__(self, stock_holder_tuple=None):
        self.id = 0
        self.stock_code = ""
        self.date = ""
        self.type = ""
        self.number = 0
        self.hold = 0
        self.ratio = 0
        self.created = ""
        self.modified = ""

        if stock_holder_tuple is None:
            return

        self.set_id(stock_holder_tuple[0])
        self.set_stock_code(stock_holder_tuple[DatabaseContract.StockHolder.stock_code.value])
        self.set_date(stock_holder_tuple[DatabaseContract.StockHolder.date.value])
        self.set_type(stock_holder_tuple[DatabaseContract.StockHolder.type.value])
        self.set_number(stock_holder_tuple[DatabaseContract.StockHolder.nubmer.value])
        self.set_hold(stock_holder_tuple[DatabaseContract.StockHolder.hold.value])
        self.set_ratio(stock_holder_tuple[DatabaseContract.StockHolder.ratio.value])
        self.set_created(stock_holder_tuple[DatabaseContract.StockHolder.created.value])
        self.set_modified(stock_holder_tuple[DatabaseContract.StockHolder.modified.value])

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
            result = tuple((self.id, self.stock_code,
                            self.date, self.type, self.number, self.hold, self.ratio,
                            self.created, self.modified))
        else:
            result = tuple((self.stock_code,
                            self.date, self.type, self.number, self.hold, self.ratio,
                            self.created, self.modified))
        return result

    @staticmethod
    def get_delete_sql():
        delete_sql = "DELETE FROM stock_holder WHERE stock_code = ?"
        return delete_sql

    @staticmethod
    def get_insert_sql():
        insert_sql = "INSERT INTO stock_holder (stock_code," \
                     "date, type, number, hold, ratio," \
                     "created, modified)" \
                     " VALUES(?," \
                     "?,?,?,?,?," \
                     "?,?)"
        return insert_sql
