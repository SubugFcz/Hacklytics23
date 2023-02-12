from django import forms
    
class StockDateInputForm(forms.Form):
    stockDate = forms.CharField(min_length=20)