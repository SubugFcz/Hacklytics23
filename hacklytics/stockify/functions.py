import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import talib as ta

def plotRSI(data, name):
    data_copy = data.copy()
    data_copy['close_5day_ave']=data_copy.Close.rolling(100).mean()
    data_copy['rsi'] = ta.RSI(data['Close'])
    fig, axis = plt.subplots(2, 1, gridspec_kw={"height_ratios": [3, 1]}, figsize=(10,6))
    axis[0].plot(data['Date'], data['Close'])
    axis[0].plot(data_copy['Date'], data_copy['close_5day_ave'])
    axis[1].axhline(y=70, color='r', linestyle="--")
    axis[1].axhline(y=35, color='g', linestyle="--")
    axis[1].plot(data_copy['Date'], data_copy['rsi'])
    axis[0].set_title(f"Close Price - {name}")
    axis[1].set_title(f"RSI - {name}")

def plotOBV(data, name):
    data_copy = data.copy()
    data_copy['obv'] = ta.OBV(data['Close'],data['Volume'])
    data_copy['obv_EMA'] = ta.EMA(data_copy['obv'])
    plt.plot(data_copy['Date'], data_copy['obv_EMA'])
    plt.plot(data_copy['Date'], data_copy['obv'])
    plt.title(f"On Balance Volume - {name}")

