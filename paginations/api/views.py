from django.shortcuts import render

# Create your views here.
from api.models import *
from api.serializers import *
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

# class MyPagenumber(PageNumberPagination):
#     page_size = 1 #maximum data in a page to display and without giving this pagination won't work
#     page_query_param = 'kalim' #to search the page no in the url
#     page_size_query_param = 'client' #to search the no of datas to be displayed by the client in url
#     max_page_size = 4 #this is used by the clients to serach in the url and setting the maximum datas to be displayed if they entered more it won't be displayed 
#     last_page_strings = 'last' #to search for the last page using this given string

# class MyLimitOffset(LimitOffsetPagination):
#     #limit and offset we can give in urls to set how many datas and from which data(given no+1) to be displayed respectively
#     default_limit = 5 #no of datas to be displayed
#     limit_query_param = 'kalim' #with this string only we can set the data in the url by default it is limit
#     offset_query_param = 'myoffset' #with this string only we can search from which data it has to be displayed by default it is offset
#     max_limit = 5 #maximum datas to be displayed in a page

class MyCursor(CursorPagination):
    #this pagination works based on the timestamp means when we created the object if we didn't give that it throws an error for that we have to use ordering fro any of the column we created to check this comment ordering and see the result
    page_size = 10
    ordering = 'Sno' #it'll show based on this order

class student(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = MyPagenumber #this is custom pagination to over ride the values from PageNumberPagination we cant directly use any paginations
    # pagination_class = MyLimitOffset #this is custom pagination to over ride the values from PageNumberPagination we cant directly use any paginations and this is specific paginations and we want generic we can include it in settings.py in the vauiable rest_framework
    pagination_class = MyCursor #this is custom pagination to over ride the values from PageNumberPagination we cant directly use any paginations

