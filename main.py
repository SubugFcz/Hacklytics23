import sys
import pandas as pd
import os
import numpy as np
import functions as fn
import matplotlib.pyplot as plt

# List of 10 more .csv files
files = ['AAPL.csv', 'ADBE.csv', 'AMZN.csv', 'CSCO.csv', 'FTNT.csv', 
         'MSFT.csv', 'MU.csv', 'NFLX.csv', 'NVDA.csv','STX.csv']
names = ['Apple', 'Adobe', 'Amazon', 'Cisco', 'Ford Motor', 
         'Microsoft', 'Micron', 'Netflix', 'Nvidia','Seagate Technology']

# Define the folder where the PNG files will be saved
folder = 'images'

# Check if the folder exists, otherwise create it
if not os.path.exists(folder):
    os.makedirs(folder)

if __name__ == '__main__':
    for file, name in zip(files, names):
        file = os.path.join(sys.path[0], file)
        d = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
        df = pd.DataFrame(data=d, columns=['Date', 'Close'])
        df2 = pd.DataFrame(data=d, columns=['Date', 'Volume', 'Close'])
        df1 = df.iloc[200:250]
        df3 = df2.iloc[200:250]

        fn.plotOBV(df3, name)
        plt.savefig(os.path.join(folder, f'{name}_OBV.png'))
        plt.close()

        fn.plotRSI(df1, name)
        plt.savefig(os.path.join(folder, f'{name}_RSI.png'))
        plt.close()