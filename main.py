import sys

import pandas as pd
import os

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
    return f'The best time to buy is at {minDate} with price ${minPrice} ' \
           f'and we can sell at {maxDate} with price ${maxPrice}. Therefore, ' \
           f'we have {profit}% profit'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = os.path.join(sys.path[0], 'AAPL.csv')
    d = pd.read_csv(file)
    df = pd.DataFrame(data=d, columns=['Date', 'Close'])
    #df1 = df.iloc[0:10400]
    closeList = df.values.tolist()

    print(best(closeList))
