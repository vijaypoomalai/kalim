from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from app.models import *
from app.serializers import *

# class Dummy(APIView):
#     authentication_classes=[TokenAuthentication]
#     permission_classes=[IsAuthenticated]

#     def get(self,request):
#         return Response({'msg':'Succesfulll...'})

class StudentViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    #eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM1MjE2MDY2LCJpYXQiOjE3MzUyMTU5NDYsImp0aSI6IjhkNGYyMjQ0MTEwMzQ2MTY4OTYxYmM1M2MzNjE2NjJhIiwidXNlcl9pZCI6MX0.Mm-xsOrGvSqSQjNcKmTBkccUWv14RvOqWxMVzyX6nfQ
