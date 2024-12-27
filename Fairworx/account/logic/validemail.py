# # from django.shortcuts import render

# # # Create your views here.
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from django.contrib.auth import authenticate

# # from rest_framework import viewsets, status

# # from rest_framework.response import Response

# # from rest_framework.decorators import action

# # from .serializers import UserSerializer

# # # class MyView(APIView):
# # #     def get(self, request, *args, **kwargs):

# # class LoginViewSet(viewsets.ViewSet):

# #     def create(self, request):

# #         username = request.data.get('username')

# #         password = request.data.get('password')

# #         user = authenticate(username=username, password=password)

# #         if user is not None:

# #             serializer = UserSerializer(user)

# #             return Response(serializer.data, status=status.HTTP_200_OK)

# #         else:

# #             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



# from django.shortcuts import render

# from rest_framework.decorators import api_view

# from rest_framework.response import Response

# from .serializers import LoginSerializers
# from django.contrib.auth import authenticate



# @api_view(['GET'])

# def login(request):

#     if request.method == 'GET':

#         serializer = LoginSerializers(data=request.data)

#         if serializer.is_valid():

#             user = serializer.validated_data

#             # Authenticate user (check password)

#             if authenticate(username=user['username'], password=user['password']):

#                 # Generate a JWT token if needed

#                 return Response({'message': 'Login successful!'})

# #             else:

# #                 return Response({'error': 'Invalid credentials'}, status=401)

# #         else:

# #             return Response(serializer.errors, status=400)


# # views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserLoginSerializer
from .serializers import UserPassword

# class login(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = UserLoginSerializer(data=request.data)
        
#         if serializer.is_valid():
#             user = serializer.validated_data['user']  # This will work because we added 'user' in the serializer
#             return Response({
#                 'message': 'Login successful!',
#                 'user_id': user.id
#             }, status=status.HTTP_200_OK)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py (for debugging)
class login(APIView):
    def get(self, request, *args, **kwargs):
        print("Request Data:", request.data)  # Debugging line
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({'message': 'Login successful!','user_id': user[0].id}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, *args, **kwargs):
        print("Request Data:", request.data)  # Debugging line
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({'message': 'Inserted successful!','user_id': user[0].id}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, *args, **kwargs):
        print("Request Data:", request.data)  # Debugging line
        serializer = UserPassword(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({
                'message': 'Password Updated successful!',
                'user_id': user[0].id
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
