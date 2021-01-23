# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:30:56 2019

@author: ADMIN
"""
import glob
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas
from matplotlib import dates as mdates
# from matplotlib.finance import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc  # pip install --upgrade mplfinance

import Constants
import Financial

stock_index = 0
stock_tuple_list = None

data = np.linspace(1, 100)
power = 0


def draw_stock_data(stock, draw_candle_stick=True, period=Constants.MONTH, save_fig=False):
    # read and reformat data

    stock_data_dict = pandas.read_csv(Financial.get_stock_data_file_name(stock), parse_dates=True, index_col=0)
    stock_data_dict.reset_index(inplace=True)
    stock_data_dict['date'] = mdates.date2num(stock_data_dict['date'])

    # setup moving average models

    x = stock_data_dict['date']
    roi = stock_data_dict['roi']

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

    financial_data_file_name = Financial.get_financial_data_file_name(stock)
    if not os.path.exists(financial_data_file_name):
        print(financial_data_file_name + " not exist, return")
        return

    financial_data_dict = pandas.read_csv(Financial.get_financial_data_file_name(stock), parse_dates=True, index_col=0)
    financial_data_dict.reset_index(inplace=True)
    financial_data_dict['date'] = mdates.date2num(financial_data_dict['date'])

    x1 = financial_data_dict['date']
    roe = financial_data_dict['roe']
    book_value_per_share = financial_data_dict['book_value_per_share']
    net_profit_per_share = financial_data_dict['net_profit_per_share'] * 10
    cash_flow_per_share = financial_data_dict['cash_flow_per_share']

    total_current_assets = financial_data_dict['total_current_assets']
    total_assets = financial_data_dict['total_assets']
    total_long_term_liabilities = financial_data_dict['total_long_term_liabilities']
    main_business_income = financial_data_dict['main_business_income']
    financial_expenses = financial_data_dict['financial_expenses']
    net_profit = financial_data_dict['net_profit']
    # roe = financial_data_dict['roe']

    share_bonus_file_name = Financial.get_share_bonus_file_name(stock)
    if not os.path.exists(share_bonus_file_name):
        print(share_bonus_file_name + " not exist, return")
        return

    share_bonus_dict = pandas.read_csv(share_bonus_file_name, parse_dates=True, index_col=0)
    share_bonus_dict.reset_index(inplace=True)
    share_bonus_dict['date'] = mdates.date2num(share_bonus_dict['date'])

    x2 = share_bonus_dict['date']
    dividend = share_bonus_dict['dividend']

    share_holder_file_name = Financial.get_share_holder_file_name(stock)
    if not os.path.exists(share_holder_file_name):
        print(share_holder_file_name + " not exist, return")
        return

    share_holder_dict = pandas.read_csv(share_holder_file_name, parse_dates=True, index_col=0)
    share_holder_dict.reset_index(inplace=True)
    share_holder_dict['date'] = mdates.date2num(share_holder_dict['date'])

    x3 = share_holder_dict['date']
    holder_number = share_holder_dict['number']
    share_ratio = share_holder_dict['ratio']

    # plot

    fig, (ax1, ax3) = plt.subplots(2, sharex=True, figsize=(10, 12))

    # plot candlestick, SAM, EMA in subplot_1
    if draw_candle_stick:
        candlestick_ohlc(ax1, stock_data_dict.values, width=0.5, colorup='r', colordown='g')
        # p1 = ax.plot(x, EMA_1, label='EMA(' + str(EMA_1_span) + ')')
        # p2 = ax.plot(x, EMA_2, label='EMA(' + str(EMA_2_span) + ')')
        # p3 = ax.plot(x, SMA_2, label='SMA(' + str(SMA_2_span) + ')')

    ax1.step(x1, roe, label='Roe')
    ax1.step(x1, cash_flow_per_share, label='CashFlowPerShare')
    ax1.step(x1, net_profit_per_share, label='NetProfitPerShare')
    ax1.step(x1, book_value_per_share, label='BookValuePerShare')
    ax1.step(x2, dividend, label='Dividend')
    ax1.step(x3, holder_number, label='HolderNumber')
    ax1.step(x3, share_ratio, label='ShareRatio')
    ax1.step(x, roi, label='ROI')

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
    ax3.plot(x1, financial_expenses, label='FinancialExpenses')
    ax3.plot(x1, net_profit, label='NetProfit')
    # ax3.plot(x1, roe, label='ROE')

    ax3.axhline(0, color='gray', linestyle='--')
    ax3.set_xlabel('date')
    ax3.set_ylabel('MACD', fontsize=16)
    ax3.legend()

    # # Pandas 无法显示中文问题 解决方案##
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    plt.title(stock.to_string())

    if save_fig:
        fig.savefig(Constants.DATA_FIGURE_PATH + stock.get_name())
        plt.close(fig)
    else:
        plt.show()


def delete_figure_files():
    print(delete_figure_files.__name__)
    if not os.path.exists(Constants.DATA_FIGURE_PATH):
        return

    files = glob.glob(Constants.DATA_FIGURE_PATH + "*.*", recursive=True)
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))
    return


def draw(where=None, order=None, sort=None, draw_candle_stick=True, save_fig=False):
    global stock_index
    global stock_tuple_list

    if save_fig:
        delete_figure_files()

    stock_tuple_list = Financial.select(where, order, sort)

    index = -1
    for stock_tuple in stock_tuple_list:
        index = index + 1

        stock = Financial.Stock(stock_tuple)
        if stock is None:
            continue

        if not Financial.check_out(stock):
            continue

        print(stock.to_string())

        Financial.write_to_file(stock)

        draw_stock_data(stock, draw_candle_stick=draw_candle_stick, save_fig=save_fig)