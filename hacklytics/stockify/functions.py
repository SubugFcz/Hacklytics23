import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import talib as ta
from StockName import stockNameDict
from django.conf import settings

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

def dateToDf(dateStart, dateEnd):
    returnList = list()
    for fileName in list(stockNameDict.keys()):
        file = os.path.join(settings.BASE_DIR, f"stockify/{fileName}.csv")
        d = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
        #df = pd.DataFrame(data=d, columns=['Date', 'Close'])
        df2 = pd.DataFrame(data=d, columns=['Date', 'Volume', 'Close'])
        df2['rsi'] = ta.RSI(df2['Close'])
        df2['obv'] = ta.OBV(df2['Close'],df2['Volume'])
        df2['obv_EMA'] = ta.EMA(df2['obv'])
        rsiMean = df2['rsi'].mean()
        obvMean = df2['obv'].mean()
        emaMean = df2['obv_EMA'].mean()
        returnList.append(dict({
            "name": stockNameDict.get(fileName),
            "rsi": rsiMean,
            "obv": obvMean,
            "ema": emaMean})
        )
    return returnList


