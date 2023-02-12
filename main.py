import sys
import pandas as pd
import os
import numpy as np
import functions as fn

# List of 10 more .csv files
files = ['file1.csv', 'file2.csv', 'file3.csv', 'file4.csv', 'file5.csv', 
         'file6.csv', 'file7.csv', 'file8.csv', 'file9.csv']

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = os.path.join(sys.path[0], 'AAPL.csv')
    d = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
    df = pd.DataFrame(data=d, columns=['Date', 'Close'])
    df2 = pd.DataFrame(data=d, columns=['Date', 'Volume', 'Close'])
    df1 = df.iloc[10200:10500]
    df3 = df2.iloc[10200:10500]
    #closeList = df1.values.tolist()
    fn.plotOBV(df3)
    fn.plotRSI(df1)
    
