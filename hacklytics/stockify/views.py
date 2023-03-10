
from django.shortcuts import render, redirect
from .functions import *
from django.conf import settings
import os
import pandas as pd
from .forms import *


# Create your views here.
def welcomePage(response):
    if response.method == "POST":
        form = StockDateInputForm(response.POST)
        if form.is_valid():
            stockDate1 = str(form.cleaned_data['stockDate'])
            return redirect(f"/stockify/stock/{stockDate1}")
    else:
        form = StockDateInputForm()

    return render(response, "stockify/welcomePage.html", {"form": form})#1

def stockPage(response, stockDate):
    dates = stockDate.split(",")  
    returnDf = superFunction(dates[0], dates[1])
    #04-02-2021,15-05-2021
    returnList = returnDf.values.tolist()
    return render(response, "stockify/stockPage.html", {"stockDate": stockDate, "myItems": returnList})
    

