import sys

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

def plotRollingAve(data):
    data_copy = data.copy()
    data_copy['close_5day_ave']=data_copy.Close.rolling(100).mean()

    #sns.lineplot(data=data, x='Date', y='Close', errorbar=None)
    #sns.lineplot(data=data_copy, x='Date', y='close_5day_ave', errorbar=None)
    #plt.xlabel('Date', size=14)
    #plt.ylabel('Close', size=14)



    fig, axis = plt.subplots(2, 1, gridspec_kw={"height_ratios": [3, 1]}, figsize=(10,6))
    axis[0].plot(data['Date'], data['Close'])
    axis[0].plot(data_copy['Date'], data_copy['close_5day_ave'])
    axis[1].axhline(y=70, color='r', linestyle="--")
    axis[1].axhline(y=30, color='g', linestyle="--")
    #axis[1].plot(data_copy['rsi'])

    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = os.path.join(sys.path[0], 'AAPL.csv')
    d = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
    df = pd.DataFrame(data=d, columns=['Date', 'Close'])
    #df1 = df.iloc[0:10500]
    #closeList = df1.values.tolist()

    plotRollingAve(df)
