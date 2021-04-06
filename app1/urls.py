from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('selectCountry', views.SingleCountry, name="SingleCountry")
]