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
import favorite
import financial

import numpy as np

stock_index = 0
stock_tuple_list = None

data = np.linspace(1, 100)
power = 0


def draw_stock_data(stock, period=constant.MONTH):
    # read and reformat data

    stock_data_dict = pandas.read_csv(financial.get_stock_data_file_name(stock), parse_dates=True, index_col=0)
    stock_data_dict.reset_index(inplace=True)
    stock_data_dict['date'] = mdates.date2num(stock_data_dict['date'].astype(datetime.date))

    # setup moving average models

    x = stock_data_dict['date']

    #
    # EMA_1_span = 7
    # EMA_1 = stock_data['Close'].ewm(span=EMA_1_span, min_periods=EMA_1_span).mean()
    #
    # EMA_2_span = 30
    # EMA_2 = stock_data['Close'].ewm(span=EMA_2_span, min_periods=EMA_2_span).mean()
    #
    # SMA_2_span = EMA_2_span
    # SMA_2 = stock_data['Close'].rolling(window=SMA_2_span, center=False).mean()
    #
    # MACD = EMA_1 - EMA_2

    financial_data_dict = pandas.read_csv(financial.get_financial_data_file_name(stock), parse_dates=True, index_col=0)
    financial_data_dict.reset_index(inplace=True)
    financial_data_dict['date'] = mdates.date2num(financial_data_dict['date'].astype(datetime.date))

    x1 = financial_data_dict['date']
    book_value_per_share = financial_data_dict['book_value_per_share']
    earnings_per_share = financial_data_dict['earnings_per_share']
    cash_flow_per_share = financial_data_dict['cash_flow_per_share']
    book_value_per_share_rate = financial_data_dict['book_value_per_share_rate']

    total_current_assets = financial_data_dict['total_current_assets']
    total_assets = financial_data_dict['total_assets']
    total_long_term_liabilities = financial_data_dict['total_long_term_liabilities']
    main_business_income = financial_data_dict['main_business_income']
    financial_expenses = financial_data_dict['financial_expenses']
    net_profit = financial_data_dict['net_profit']
    roe = financial_data_dict['roe']

    share_bonus_dict = pandas.read_csv(financial.get_share_bonus_file_name(stock), parse_dates=True, index_col=0)
    share_bonus_dict.reset_index(inplace=True)
    share_bonus_dict['date'] = mdates.date2num(share_bonus_dict['date'].astype(datetime.date))

    x2 = share_bonus_dict['date']
    dividend = share_bonus_dict['dividend']

    # plot

    fig, (ax1, ax3) = plt.subplots(2, sharex=True, figsize=(10, 12))

    # plot candlestick, SAM, EMA in subplot_1
    candlestick_ohlc(ax1, stock_data_dict.values, width=0.5, colorup='r', colordown='g')
    # p1 = ax.plot(x, EMA_1, label='EMA(' + str(EMA_1_span) + ')')
    # p2 = ax.plot(x, EMA_2, label='EMA(' + str(EMA_2_span) + ')')
    # p3 = ax.plot(x, SMA_2, label='SMA(' + str(SMA_2_span) + ')')

    ax1.step(x1, cash_flow_per_share, label='CashFlowPerShare')
    ax1.step(x1, earnings_per_share * 10.0, label='EarningsPerShare')
    ax1.step(x1, book_value_per_share, label='BookValuePerShare')
    ax1.step(x2, dividend, label='Dividend')

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mdates.MonthLocator([1, 4, 7, 10]))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%b '%y"))
    ax1.set_ylabel('Price', fontsize=16)
    ax1.legend()

    # plot volume in subplot_2
    # ax2.bar(x, stock_data_dict['volume'])
    # ax2.set_ylabel('volume', fontsize=16)

    # plot MACD in subplot_3
    # ax3.plot(x, MACD, label='MACD (' + 'EMA(' + str(EMA_1_span) + '), ' + 'EMA(' + str(EMA_2_span) + '))')

    # ax3.plot(x1, total_current_assets, label='TotalCurrentAssets')
    # ax3.plot(x1, total_assets, label='TotalAssets')
    ax3.plot(x1, total_long_term_liabilities, label='TotalLongTermLiabilities')
    ax3.plot(x1, main_business_income, label='MainBusinessIncome')
    # ax3.plot(x1, financial_expenses, label='FinancialExpenses')
    ax3.plot(x1, net_profit, label='NetProfit')
    # ax3.plot(x1, roe, label='ROE')

    ax3.axhline(0, color='gray', linestyle='--')
    ax3.set_xlabel('date')
    ax3.set_ylabel('MACD', fontsize=16)
    ax3.legend()

    # # Pandas 无法显示中文问题 解决方案##
    plt.rcParams['font.sans-serif'] = ['KaiTi']
    plt.rcParams['font.serif'] = ['KaiTi']

    title = stock.name + " " + stock.code \
            + " pe " + str(stock.pe)\
            + " pb " + str(stock.pb) \
            + " dividend " + str(stock.dividend) \
            + " yield " + str(round(stock.dividend_yield, 2)) \
            + " rating " + str(stock.rating)\
            + " favorite " + str(stock.favorite)
    plt.title(title)

    plt.show()

    # ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
    #
    # for label in ax1.xaxis.get_ticklabels():
    #     label.set_rotation(45)
    #
    # ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    # ax1.grid(True)
    #
    # candlestick_ohlc(ax1, df.values, width=5, colorup='r', colordown='g')
    #
    # # Pandas 无法显示中文问题 解决方案##
    # plt.rcParams['font.sans-serif'] = ['KaiTi']
    # plt.rcParams['font.serif'] = ['KaiTi']
    #
    # title = name + " " + code
    # plt.title(title)
    # plt.xlabel('date')
    # plt.ylabel('Price')
    #
    # plt.show()


def draw(where=None, order=None, sort=None):
    global stock_index
    global stock_tuple_list

    stock_tuple_list = financial.select(where, order, sort)

    index = -1
    for stock_tuple in stock_tuple_list:
        index = index + 1

        stock = financial.Stock(stock_tuple)
        if stock is None:
            continue

        print(stock.code, stock.name, "price:" + str(stock.price), "net:" + str(stock.net), "dividend:" + str(stock.dividend),
              "yield:" + str(stock.dividend_yield), "rating:" + str(stock.rating), "favorite:" + str(stock.favorite))

        financial.write_to_file(stock)

        draw_stock_data(stock)


def on_keyboard(event):
    global data
    global power

    global stock_index
    global stock_tuple_list

    if event.key == 'right':
        power += 1
        if power > len(stock_tuple_list) - 1:
            power = len(stock_tuple_list) - 1

        stock_index += 1
        if stock_index > len(stock_tuple_list) - 1:
            stock_index = len(stock_tuple_list) - 1
            return
    elif event.key == 'left':
        power -= 1
        if power < 0:
            power = 0

        stock_index -= 1
        if stock_index < 0:
            stock_index = 0
            return

    plt.clf()

    plt.plot(data ** power)

    stock = financial.Stock(stock_tuple_list[stock_index])
    financial.write_to_file(stock)

    plt.draw()


def test(where=None, order=None, sort=None):
    global data
    global power
    global stock_index
    global stock_tuple_list

    stock_index = 0
    stock_tuple_list = financial.select(where, order, sort)

    if stock_tuple_list is None:
        return

    stock = financial.Stock(stock_tuple_list[stock_index])
    financial.write_to_file(stock)

    data = np.linspace(1, 100)
    power = 0
    plt.plot(data ** power)

    plt.gcf().canvas.mpl_connect('key_press_event', on_keyboard)

    plt.show()
