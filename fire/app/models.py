from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    first_name=models.CharField(max_length=100,blank=False)
    last_name=models.CharField(max_length=100,blank=True)
    email=models.EmailField(blank=False,max_length=100,unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

