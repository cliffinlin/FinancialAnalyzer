# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:30:56 2019

@author: ADMIN
"""

import datetime
import pandas
import matplotlib.pyplot as plt

from matplotlib import dates as mdates
from matplotlib.finance import candlestick_ohlc

import constant
import draw
import financial


if __name__ == "__main__":
    # financial.download()
    # financial.analyze()
    # draw.draw("rating > 0 ", "bvpsr", "DESC")#where=None, order=None, sort=None #"DESC""ASC"
    draw.draw("rating=7 AND bvpsr>0", "bvpsr", "DESC")#where=None, order=None, sort=None #"DESC""ASC"
    # draw.draw("rating > 0 AND bvpsr > 100", "bvpsr", "DESC")  # where=None, order=None, sort=None #"DESC""ASC"
