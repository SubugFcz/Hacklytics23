import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import talib as ta
from .StockName import stockNameDict
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

def dateToDf():
    returnList = list()
    for fileName in list(stockNameDict.keys()):
        file = os.path.join(settings.BASE_DIR, f"stockify/csvfiles/{fileName}.csv")
        d = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
        #df = pd.DataFrame(data=d, columns=['Date', 'Close'])
        df2 = pd.DataFrame(data=d, columns=['Date', 'Volume', 'Close'])
        df2['rsi'] = ta.RSI(df2['Close'])
        df2['obv'] = ta.OBV(df2['Close'],df2['Volume'])
        df2['obv_EMA'] = ta.EMA(df2['obv'])
        currRSI = df2['rsi'].loc['01-08-2021']
        currOBV = df2['obv'].loc['01-08-2021']
        currEMA = df2['obv_EMA'].loc['01-08-2021']
        #rsiMean = df2['rsi'].mean()
        #obvMean = df2['obv'].mean()
        #emaMean = df2['obv_EMA'].mean()
        returnList.append(dict({
            "name": stockNameDict.get(fileName),
            "rsi": currRSI,
            "obv": currOBV,
            "ema": currEMA})
        )
    return returnList

files = ['AAPL.csv', 'ADBE.csv', 'AMZN.csv', 'CSCO.csv', 'FTNT.csv', 
         'MSFT.csv', 'MU.csv', 'NFLX.csv', 'NVDA.csv','STX.csv']
names = ['Apple', 'Adobe', 'Amazon', 'Cisco', 'Ford Motor', 
         'Microsoft', 'Micron', 'Netflix', 'Nvidia','Seagate Technology']

def extract_data(start_date, end_date, file):
    # Read the CSV file into a pandas dataframe
    df = pd.read_csv(os.path.join(settings.BASE_DIR, f"stockify/csvfiles/{file}"))
    
    # Convert the "Date" column to datetime format
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
    
    # Filter the dataframe to include only rows between the start and end dates
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    df = df.loc[mask]
    
    # Select only the columns "Date", "Close", and "Volume"
    df = df[["Date", "Close", "Volume"]]
    
    return df
    

def plotRSI(date1, date2, file):
    # Call the extract_data function to get the data for the specified date range
    dg = extract_data(date1, date2, file)
    
    # Calculate the RSI using ta-lib
    close = dg["Close"].values
    rsi = ta.RSI(close)

    # Add the RSI values to the dataframe
    dg["RSI"] = pd.Series(rsi, index=dg.index)
    avg_rsi = dg["RSI"].mean()
    
    return avg_rsi
    

def plotOBV(date1, date2, file):
    dg = extract_data(date1, date2, file)
    dg['OBV'] = ta.OBV(dg['Close'],dg['Volume'])
    dg['obv_EMA'] = ta.EMA(dg['OBV'])
    
    return dg[['Date', 'OBV', 'obv_EMA']]

def sumOBV(df):
    sum_OBV = df['OBV'].sum()
    sum_obv_EMA = df['obv_EMA'].sum()
    
    result = sum_OBV - sum_obv_EMA
    
    return result

def generate_summary_df(date1, date2):
    summary_data = []
    for i, file in enumerate(files):
        avg_rsi = plotRSI(date1, date2, file)
        obv_df = plotOBV(date1, date2, file)
        result = sumOBV(obv_df)
        
        summary_data.append([names[i], avg_rsi, result])
        
    summary_df = pd.DataFrame(summary_data, columns=["Name", "avg_rsi", "obvdiff"])
    return summary_df

def add_rank_column(date1, date2):
    df = generate_summary_df(date1, date2)
    df['Rank_RSI'] = df['avg_rsi'].rank(ascending=False, method='dense')
    df['Rank_RSI'] = (df['Rank_RSI'].max() - df['Rank_RSI']) + 1
    df['Rank_OBV'] = df['obvdiff'].rank(ascending=True, method='dense')
    df['Rank_OBV'] = (df['Rank_OBV'].max() - df['Rank_OBV']) + 1
    return df
   
def superFunction(date1, date2):
    df = add_rank_column(date1, date2)
    df['Rank_Sum'] = df['Rank_RSI'] + df['Rank_OBV']
    df['Rank_Sum'] = df['Rank_Sum'].rank(ascending=False, method='dense')
    df['Rank_Sum'] = (df['Rank_Sum'].max() - df['Rank_Sum']) + 1
    return df



