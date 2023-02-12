import sys

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import talib as ta

def best(arr):
    left, right = 0, 1
    minPrice, maxPrice = 0, 0
    minDate, maxDate = "", ""
    while left < right and right < len(arr):
        if arr[left][1] > arr[right][1]:
            left = right
            minPrice = arr[left][1]
            minDate = arr[left][0]
        elif maxPrice < arr[right][1]:
            maxPrice = arr[right][1]
            maxDate = arr[right][0]
        right += 1
    profit = (maxPrice / minPrice) * 100
    return f'The best time to buy is at {minDate} with price ${float(round(minPrice,2))} ' \
           f'and we can sell at {maxDate} with price ${float(round(maxPrice, 2))}. Therefore, ' \
           f'we have {float(round(profit,2))}% profit'

def plotRSI(data):
    data_copy = data.copy()
    data_copy['close_5day_ave']=data_copy.Close.rolling(100).mean()
    data_copy['rsi'] = ta.RSI(data['Close'])

    fig, axis = plt.subplots(2, 1, gridspec_kw={"height_ratios": [3, 1]}, figsize=(10,6))
    axis[0].plot(data['Date'], data['Close'])
    axis[0].plot(data_copy['Date'], data_copy['close_5day_ave'])
    axis[1].axhline(y=70, color='r', linestyle="--")
    axis[1].axhline(y=35, color='g', linestyle="--")
    axis[1].plot(data_copy['Date'], data_copy['rsi'])

    plt.show()

def plotOBV(data):
    data_copy = data.copy()
    data_copy['obv'] = ta.OBV(data['Close'],data['Volume'])
    data_copy['obv_EMA'] = ta.EMA(data_copy['obv'])

    plt.plot(data_copy['Date'], data_copy['obv_EMA'])
    plt.plot(data_copy['Date'], data_copy['obv'])

    plt.show()