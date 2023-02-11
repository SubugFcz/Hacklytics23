
from django.shortcuts import render
from .functions import *
from django.conf import settings
import os
import pandas as pd


# Create your views here.
def welcomePage(response):
    file = os.path.join(settings.BASE_DIR, "stockify/csvfiles/AAPL.csv")
    d = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
    df = pd.DataFrame(data=d, columns=['Date', 'Close'])
    closeList = df.values.tolist()
    return render(response, "stockify/index.html",{"myItems": closeList})

