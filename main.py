import sys

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

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

def plotRegress(arr):
    x = []
    y = []
    for i in range(len(arr)):
        x.append(i)
        y.append(arr[i][1])
    x = np.array(x)
    y = np.array(y)

    a, b = np.polyfit(x, y, 1)

    plt.plot(x, y, 'o', label='Original data')
    plt.plot(x, a*x + b, 'r', label='Fitted line')
    plt.legend()
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = os.path.join(sys.path[0], 'AAPL.csv')
    d = pd.read_csv(file)
    df = pd.DataFrame(data=d, columns=['Date', 'Close'])
    df1 = df.iloc[0:5]
    closeList = df1.values.tolist()

    plotRegress(closeList)
    # print(best(closeList))
