
from django.shortcuts import render
from .functions import *

# Create your views here.
def welcomePage(response):
    return render(response, "stockify/index.html",{})

