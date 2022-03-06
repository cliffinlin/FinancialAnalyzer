# -*- coding: utf-8 -*-
import DatabaseContract
from DatabaseTable import DatabaseTable


class StockData(DatabaseTable):
    def __init__(self, stock_data_tuple=None):
        DatabaseTable.__init__(self)

        self.stock_id = ""
        self.date = ""
        self.time = ""
        self.period = ""
        self.open = 0
        self.high = 0
        self.low = 0
        self.close = 0
        self.amplitude = 0
        self.vertex_high = 0
        self.vertex_low = 0
        self.overlap = 0
        self.overlap_high = 0
        self.overlap_low = 0
        self.average5 = 0
        self.average10 = 0
        self.dif = 0
        self.dea = 0
        self.histogram = 0
        self.sigma_histogram = 0
        self.roi = 0
        self.pe = 0
        self.pb = 0
        self.dividend_yield = 0
        self.level = 0
        self.direction = 0
        self.vertex = 0
        self.divergence = 0
        self.action = ""

        self.set(stock_data_tuple)

    def set(self, stock_data_tuple):
        if stock_data_tuple is None:
            return

        DatabaseTable.set(self, stock_data_tuple[DatabaseContract.StockDataColumn.id.value],
                          stock_data_tuple[DatabaseContract.StockDataColumn.created.value],
                          stock_data_tuple[DatabaseContract.StockDataColumn.modified.value])

        self.set_stock_id(stock_data_tuple[DatabaseContract.StockDataColumn.stock_id.value])
        self.set_date(stock_data_tuple[DatabaseContract.StockDataColumn.date.value])
        self.set_time(stock_data_tuple[DatabaseContract.StockDataColumn.time.value])
        self.set_period(stock_data_tuple[DatabaseContract.StockDataColumn.period.value])
        self.set_open(stock_data_tuple[DatabaseContract.StockDataColumn.open.value])
        self.set_high(stock_data_tuple[DatabaseContract.StockDataColumn.high.value])
        self.set_low(stock_data_tuple[DatabaseContract.StockDataColumn.low.value])
        self.set_close(stock_data_tuple[DatabaseContract.StockDataColumn.close.value])
        self.set_amplitude(stock_data_tuple[DatabaseContract.StockDataColumn.amplitude.value])
        self.set_vertex_high(stock_data_tuple[DatabaseContract.StockDataColumn.vertex_high.value])
        self.set_vertex_low(stock_data_tuple[DatabaseContract.StockDataColumn.vertex_low.value])
        self.set_overlap(stock_data_tuple[DatabaseContract.StockDataColumn.overlap.value])
        self.set_overlap_high(stock_data_tuple[DatabaseContract.StockDataColumn.overlap_high.value])
        self.set_overlap_low(stock_data_tuple[DatabaseContract.StockDataColumn.overlap_low.value])
        self.set_average5(stock_data_tuple[DatabaseContract.StockDataColumn.average5.value])
        self.set_average10(stock_data_tuple[DatabaseContract.StockDataColumn.average10.value])
        self.set_dif(stock_data_tuple[DatabaseContract.StockDataColumn.dif.value])
        self.set_dea(stock_data_tuple[DatabaseContract.StockDataColumn.dea.value])
        self.set_histogram(stock_data_tuple[DatabaseContract.StockDataColumn.histogram.value])
        self.set_sigma_histogram(stock_data_tuple[DatabaseContract.StockDataColumn.sigma_histogram.value])
        self.set_roi(stock_data_tuple[DatabaseContract.StockDataColumn.roi.value])
        self.set_pe(stock_data_tuple[DatabaseContract.StockDataColumn.pe.value])
        self.set_pb(stock_data_tuple[DatabaseContract.StockDataColumn.pb.value])
        self.set_dividend_yield(stock_data_tuple[DatabaseContract.StockDataColumn.dividend_yield.value])
        self.set_level(stock_data_tuple[DatabaseContract.StockDataColumn.level.value])
        self.set_direction(stock_data_tuple[DatabaseContract.StockDataColumn.direction.value])
        self.set_vertex(stock_data_tuple[DatabaseContract.StockDataColumn.vertex.value])
        self.set_divergence(stock_data_tuple[DatabaseContract.StockDataColumn.divergence.value])
        self.set_action(stock_data_tuple[DatabaseContract.StockDataColumn.action.value])

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

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        if amplitude is not None:
            self.amplitude = amplitude

    def get_vertex_high(self):
        return self.vertex_high

    def set_vertex_high(self, vertex_high):
        if vertex_high is not None:
            self.vertex_high = vertex_high

    def get_vertex_low(self):
        return self.vertex_low

    def set_vertex_low(self, vertex_low):
        if vertex_low is not None:
            self.vertex_low = vertex_low

    def get_overlap(self):
        return self.overlap

    def set_overlap(self, overlap):
        if overlap is not None:
            self.overlap = overlap

    def get_overlap_high(self):
        return self.overlap_high

    def set_overlap_high(self, overlap_high):
        if overlap_high is not None:
            self.overlap_high = overlap_high

    def get_overlap_low(self):
        return self.overlap_low

    def set_overlap_low(self, overlap_low):
        if overlap_low is not None:
            self.overlap_low = overlap_low

    def get_average5(self):
        return self.average5

    def set_average5(self, average5):
        if average5 is not None:
            self.average5 = average5

    def get_average10(self):
        return self.average10

    def set_average10(self, average10):
        if average10 is not None:
            self.average10 = average10

    def get_dif(self):
        return self.dif

    def set_dif(self, dif):
        if dif is not None:
            self.dif = dif

    def get_dea(self):
        return self.dea

    def set_dea(self, dea):
        if dea is not None:
            self.dea = dea

    def get_histogram(self):
        return self.histogram

    def set_histogram(self, histogram):
        if histogram is not None:
            self.histogram = histogram

    def get_sigma_histogram(self):
        return self.sigma_histogram

    def set_sigma_histogram(self, sigma_histogram):
        if sigma_histogram is not None:
            self.sigma_histogram = sigma_histogram

    def get_roi(self):
        return self.roi

    def set_roi(self, roi):
        if roi is not None:
            self.roi = roi

    def get_pe(self):
        return self.pe

    def set_pe(self, pe):
        if pe is not None:
            self.pe = pe

    def get_pb(self):
        return self.pb

    def set_pb(self, pb):
        if pb is not None:
            self.pb = pb

    def get_dividend_yield(self):
        return self.dividend_yield

    def set_dividend_yield(self, dividend_yield):
        if dividend_yield is not None:
            self.dividend_yield = dividend_yield

    def get_level(self):
        return self.level

    def set_level(self, level):
        if level is not None:
            self.level = level

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        if direction is not None:
            self.direction = direction

    def get_vertex(self):
        return self.vertex

    def set_vertex(self, vertex):
        if vertex is not None:
            self.vertex = vertex

    def get_divergence(self):
        return self.divergence

    def set_divergence(self, divergence):
        if divergence is not None:
            self.divergence = divergence

    def get_action(self):
        return self.action

    def set_action(self, action):
        if action is not None:
            self.action = action

    def to_tuple(self, include_id=False):
        if include_id:
            result = tuple((self.id,
                            self.stock_id, self.date, self.time, self.period,
                            self.open, self.high, self.low, self.close,
                            self.amplitude, self.vertex_high, self.vertex_low, self.overlap, self.overlap_high, self.overlap_low,
                            self.average5, self.average10, self.dif, self.dea, self.histogram, self.sigma_histogram,
                            self.roi, self.pe, self.pb, self.dividend_yield,
                            self.level, self.direction, self.vertex, self.divergence,
                            self.action,
                            self.created, self.modified
                            ))
        else:
            result = tuple((
                            self.stock_id, self.date, self.time, self.period,
                            self.open, self.high, self.low, self.close,
                            self.amplitude, self.vertex_high, self.vertex_low, self.overlap, self.overlap_high, self.overlap_low,
                            self.average5, self.average10, self.dif, self.dea, self.histogram, self.sigma_histogram,
                            self.roi, self.pe, self.pb, self.dividend_yield,
                            self.level, self.direction, self.vertex, self.divergence,
                            self.action,
                            self.created, self.modified
                            ))
        return result

    @staticmethod
    def get_delete_sql():
        delete_sql = "DELETE FROM stock_data WHERE period = ? AND stock_id = ?"
        return delete_sql

    @staticmethod
    def get_insert_sql():
        insert_sql = "INSERT INTO stock_data (" \
                     "stock_id, date, time, period," \
                     "open, high, low, close," \
                     "amplitude, vertex_high, vertex_low, overlap, overlap_high, overlap_low," \
                     "average5, average10, dif, dea, histogram, sigma_histogram," \
                     "roi, pe, pb, dividend_yield," \
                     "level, direction, vertex, divergence," \
                     "action," \
                     "created, modified" \
                     ") VALUES (" \
                     "?,?,?,?," \
                     "?,?,?,?," \
                     "?,?,?,?,?,?," \
                     "?,?,?,?,?,?," \
                     "?,?,?,?," \
                     "?,?,?,?," \
                     "?," \
                     "?,?" \
                     ")"
        return insert_sql
