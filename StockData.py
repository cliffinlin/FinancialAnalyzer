# -*- coding: utf-8 -*-
import DatabaseContract


class StockData:
    def __init__(self, stock_data_tuple=None):
        self.id = 0
        self.stock_code = ""
        self.date = ""
        self.time = ""
        self.period = ""
        self.open = 0
        self.high = 0
        self.low = 0
        self.close = 0
        self.volume = 0
        self.created = ""
        self.modified = ""

        if stock_data_tuple is None:
            return

        self.set_id(stock_data_tuple[0])
        self.set_stock_code(stock_data_tuple[DatabaseContract.StockDataColumn.stock_code.value])
        self.set_date(stock_data_tuple[DatabaseContract.StockDataColumn.date.value])
        self.set_time(stock_data_tuple[DatabaseContract.StockDataColumn.time.value])
        self.set_period(stock_data_tuple[DatabaseContract.StockDataColumn.period.value])
        self.set_open(stock_data_tuple[DatabaseContract.StockDataColumn.open.value])
        self.set_high(stock_data_tuple[DatabaseContract.StockDataColumn.high.value])
        self.set_low(stock_data_tuple[DatabaseContract.StockDataColumn.low.value])
        self.set_close(stock_data_tuple[DatabaseContract.StockDataColumn.close.value])
        self.set_volume(stock_data_tuple[DatabaseContract.StockDataColumn.volume.value])
        self.set_created(stock_data_tuple[DatabaseContract.StockDataColumn.created.value])
        self.set_modified(stock_data_tuple[DatabaseContract.StockDataColumn.modified.value])

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

    def get_time(self):
        return self.time

    def set_time(self, time):
        if time is not None:
            self.time = time

    def get_period(self):
        return self.period

    def set_period(self, period):
        if period is not None:
            self.period = period

    def get_open(self):
        return self.open

    def set_open(self, open):
        if open is not None:
            self.open = open

    def get_high(self):
        return self.high

    def set_high(self, high):
        if high is not None:
            self.high = high

    def get_low(self):
        return self.low

    def set_low(self, low):
        if low is not None:
            self.low = low

    def get_close(self):
        return self.close

    def set_close(self, close):
        if close is not None:
            self.close = close

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        if volume is not None:
            self.volume = volume

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
            result = tuple((self.id, self.stock_code, self.date,
                            self.time, self.period,
                            self.open, self.high, self.low, self.close, self.volume,
                            self.created, self.modified))
        else:
            result = tuple((self.stock_code, self.date,
                            self.time, self.period,
                            self.open, self.high, self.low, self.close, self.volume,
                            self.created, self.modified))
        return result

    @staticmethod
    def get_delete_sql():
        delete_sql = "DELETE FROM stock_data WHERE period = ? AND stock_code = ?"
        return delete_sql

    @staticmethod
    def get_insert_sql():
        insert_sql = "INSERT INTO stock_data (stock_code, date," \
                     " time, period," \
                     " open, high, low, close, volume," \
                     " created, modified)" \
                     " VALUES(?,?," \
                     "?,?," \
                     "?,?,?,?,?," \
                     "?,?)"
        return insert_sql


