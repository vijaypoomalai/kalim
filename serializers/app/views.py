from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly,IsAdminUser

#class based view CRUD
# class studentcrud(APIView):
#     def get(self,request,id):
#         LSO=Student.objects.all()
#         JSO=StudentModelSerializer(LSO,many=True)
#         return Response(JSO.data)
    
#     def post(self,request,id):
#         JSO=StudentModelSerializer(data=request.data)
#         if JSO.is_valid():
#             JSO.save()
#             return Response(JSO.data)
#         return Response({'msg':'Invalid'})
    
#     def put(self,request,id):
#         # id=request.data['id']
#         GSO=Student.objects.get(Sid=id)
#         JSO=StudentModelSerializer(GSO,data=request.data)
#         if JSO.is_valid():
#             JSO.save()
#             return Response(JSO.data)
#         return Response({'msg':'Invalid'})
    
#     def patch(self,request,id):
#         GSO=Student.objects.get(Sid=id)
#         JSO=StudentModelSerializer(GSO,data=request.data,partial=True)
#         if JSO.is_valid():
#             JSO.save()
#             return Response(JSO.data)
#         return Response({'msg':'Invalid'})
    
#     def delete(self,request,id):
#         GSO=Student.objects.get(Sid=id)
#         GSO.delete()
#         return Response({'msg':'Deleted'})

#Function based view CRUD
# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def StudentCrud(request,id):   
    
#     if request.method=='GET':
#         GSO=Student.objects.all()
#         JSO=StudentModelSerializer(GSO,many=True)
#         return Response(JSO.data)
    
#     elif request.method=='POST':
#         JSO=StudentModelSerializer(data=request.data)
#         if JSO.is_valid():
#             JSO.save()
#             return Response({'msg':'Created'})
#         return Response({'msg':'Invalid'})
    
#     elif request.method=='PUT':
#         GSO=Student.objects.get(Sid=id)
#         JSO=StudentModelSerializer(GSO,data=request.data)
#         if JSO.is_valid():
#             JSO.save()
#             return Response({'msg':'Updated'})
#         return Response({'msg':'Invalid'})
    
#     elif request.method=='PATCH':
#         GSO=Student.objects.get(Sid=id)
#         JSO=StudentModelSerializer(GSO,data=request.data,partial=True)
#         if JSO.is_valid():
#             JSO.save()
#             return Response({'msg':'Updated'})
#         return Response({'msg':'Invalid'})
    
#     elif request.method=='DELETE':
#         GSO=Student.objects.get(Sid=id)
#         GSO.delete()
#         return Response({'msg':'Deleted'})

#modelviewset based view CRUD
# class StudentsCRUD(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentModelSerializer

#normal viewset based view CRUD
# class StudentViewset(viewsets.ViewSet):
#     def list(self,request):
#         LSO=Student.objects.all()
#         JSO=StudentModelSerializer(LSO,many=True)
#         return Response(JSO.data)
    
#     def retrieve(self,request,pk):
#         GSO=Student.objects.get(Sid=pk)
#         JSO=StudentModelSerializer(GSO)
#         return Response(JSO.data)
    
#     def create(self,request):
#         JSO=StudentModelSerializer(data=request.data)
#         if JSO.is_valid():
#             JSO.save()
#             return Response({'msg':'Created Successfully'})
#         return Response({'msg':'Invalid'})
    
#     def update(self,request,pk):
#         GSO=Student.objects.get(Sid=pk)
#         JSO=StudentModelSerializer(GSO,data=request.data)
#         if JSO.is_valid():
#             JSO.save()
#             return Response({'msg':'Updated Successfully'})
#         return Response({'msg':'Invalid'})
    
#     def partial_update(self,request,pk):
#         GSO=Student.objects.get(Sid=pk)
#         JSO=StudentModelSerializer(GSO,data=request.data,partial=True)
#         if JSO.is_valid():
#             JSO.save()
#             return Response({'msg':'Updated Successfully'})
#         return Response({'msg':'Invalid'})
    
#     def destroy(self,request,pk):
#         GSO=Student.objects.get(Sid=pk)
#         GSO.delete()
#         return Response({'msg':'Deleted'})

class TeacherCrud(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser]
    # permission_classes=[IsAdminUser]
    permission_classes=[IsAuthenticatedOrReadOnly]



  






