from django.urls import path, include
from . import views
urlpatterns = [
    path("home/", views.welcomePage, name="Welcome"),
    path("stock/<str:stockDate>", views.stockPage, name="Stock")
]
