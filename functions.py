import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import talib as ta

from datetime import datetime

files = ['AAPL.csv', 'ADBE.csv', 'AMZN.csv', 'CSCO.csv', 'FTNT.csv', 
         'MSFT.csv', 'MU.csv', 'NFLX.csv', 'NVDA.csv','STX.csv']
names = ['Apple', 'Adobe', 'Amazon', 'Cisco', 'Ford Motor', 
         'Microsoft', 'Micron', 'Netflix', 'Nvidia','Seagate Technology']

def extract_data(start_date, end_date):
    # Read the CSV file into a pandas dataframe
    df = pd.read_csv("data.csv")
    
    # Convert the "Date" column to datetime format
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
    
    # Filter the dataframe to include only rows between the start and end dates
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    df = df.loc[mask]
    
    # Select only the columns "Date", "Close", and "Volume"
    df = df[["Date", "Close", "Volume"]]
    
    return df
    

def plotRSI(date1, date2):
    # Call the extract_data function to get the data for the specified date range
    dg = extract_data(date1, date2)
    
    # Calculate the RSI using ta-lib
    close = dg["Close"].values
    rsi = ta.RSI(close)
    
    # Add the RSI values to the dataframe
    dg["RSI"] = pd.Series(rsi, index=dg.index)
    
    return dg[["Date", "RSI"]]
    # data_copy = data.copy()
    # data_copy['close_5day_ave']=data_copy.Close.rolling(100).mean()
    # data_copy['rsi'] = ta.RSI(data['Close'])
    # fig, axis = plt.subplots(2, 1, gridspec_kw={"height_ratios": [3, 1]}, figsize=(10,6))
    # axis[0].plot(data['Date'], data['Close'])
    # axis[0].plot(data_copy['Date'], data_copy['close_5day_ave'])
    # axis[1].axhline(y=70, color='r', linestyle="--")
    # axis[1].axhline(y=35, color='g', linestyle="--")
    # axis[1].plot(data_copy['Date'], data_copy['rsi'])
    # axis[0].set_title(f"Close Price - {name}")
    # axis[1].set_title(f"RSI - {name}")

def plotOBV(date1, date2):
    dg = extract_data(date1, date2)
    dg['OBV'] = ta.OBV(dg['Close'],dg['Volume'])
    dg['obv_EMA'] = ta.EMA(dg['obv'])

    # data_copy = data.copy()
    # data_copy['obv'] = ta.OBV(data['Close'],data['Volume'])
    # data_copy['obv_EMA'] = ta.EMA(data_copy['obv'])
    # plt.plot(data_copy['Date'], data_copy['obv_EMA'])
    # plt.plot(data_copy['Date'], data_copy['obv'])
    # plt.title(f"On Balance Volume - {name}")

