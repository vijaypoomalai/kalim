from django.contrib import admin
from django.urls import path,include
from .views import *

from rest_framework.routers import DefaultRouter

DRO=DefaultRouter()
DRO.register('StudentViewset/',StudentViewset,basename='StudentViewset')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('Dummy/',Dummy.as_view(),name='Dummy'),
    path('',include(DRO.urls)),
    
]