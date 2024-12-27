"""
URL configuration for serializers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app.views import *
from rest_framework.routers import DefaultRouter

DRO=DefaultRouter()
#for model viewset we have to create router objects for automatic url mapping
# DRO.register(r'StudentsCRUD',StudentsCRUD,basename=StudentsCRUD)
#for model viewset we have to create router objects for automatic url mapping
# DRO.register(r'StudentViewset',StudentViewset,basename=StudentViewset)
DRO.register(r'TeacherCrud',TeacherCrud,basename=TeacherCrud)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('studentcrud/<id>/',studentcrud.as_view(),name='studentcrud'),
    # path('StudentCrud/<id>',StudentCrud,name='StudentCrud'),
    # path('StudentsCRUD/',include(DRO.urls)),
    # path('StudentViewset/',include(DRO.urls)),
    path('TeacherCrud/',include(DRO.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),#this is for getting login button in the api page
]
