from django.contrib import admin
from django.urls import path
from account.logic.validemail import *

urlpatterns = [
    path('login/',login.as_view(),name='login'),
]
