# from rest_framework.serializers import Serializer
# from account.models.models import *
# class LoginSerializers(Serializer):
#     class Meta:
#         model=User

# serializers.py
# from django.contrib.auth import authenticate

from rest_framework import serializers
from account.models import *

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    print("Serializers1",email,password)

    def validate(self, attrs):
        email = attrs.get('email')  # Use .get() to avoid KeyError
        password = attrs.get('password')
        # print("Serializers2",email,password)

        if not email or not password:
            raise serializers.ValidationError("Both email and password are required.")

        user = User.objects.filter(email=email)
        # print(user)
        if user:
            if user[0].password==password:
                
                attrs['user'] = user  # Store the authenticated user in attrs
                return attrs
            else:
                raise serializers.ValidationError("Invalid Password.")
        else:
            raise serializers.ValidationError("Invalid Email.")
        # if user is None:
        #     raise serializers.ValidationError("Invalid credentials.")
        
        
class UserPassword(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    # print("Serializers1",email,password)

    def validate(self, attrs):
        email = attrs.get('email')  # Use .get() to avoid KeyError
        password = attrs.get('password')
        # print("Serializers2",email,password)

        if not email or not password:
            raise serializers.ValidationError("Both email and password are required.")

        user = User.objects.filter(email=email)
        # print(user)
        if user:
            User.objects.filter(email=email).update(password=password)
            
            attrs['user'] = user  # Store the authenticated user in attrs
            return attrs
        else:
            raise serializers.ValidationError("Invalid Email.")
        # if user is None:
        #     raise serializers.ValidationError("Invalid credentials.")
        
        
