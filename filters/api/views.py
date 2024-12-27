from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from api.models import *
from api.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

class student(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # filter_backends=[DjangoFilterBackend] #this is the module for filter
    # filterset_fields=['Sname','result'] #based on this fields we're filtering

    # filter_backends=[SearchFilter]
    # # search_fields = ['Sname']
    # search_fields = ['^Sname','city'] # (^)denotes startswith

    filter_backends = [OrderingFilter] #for all fields
    # ordering_fields = ['Sname'] #for specific fields


    # def get_queryset(self):   #to filter the data and displays the data who is passed by the user who is currently logged in and this is specific method for filtering
    #     user=self.request.user
    #     return Student.objects.filter(passby=user)