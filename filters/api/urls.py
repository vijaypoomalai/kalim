from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('student/',student.as_view(),name='student'),
]