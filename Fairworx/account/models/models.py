from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ValidationError

class User(AbstractBaseUser):
    first_name=models.CharField(max_length=100,blank=False)
    last_name=models.CharField(max_length=100,blank=True)
    email=models.EmailField(max_length=100,unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    # created_date=models.DateField(auto_now_add=True,blank=True) 
    # updated_date=models.DateField(auto_now=True,blank=True)

    USERNAME_FIELD='email'

    def clean(self):
        if not self.email.endswith("@fairworx.com") :
            raise ValidationError('Not Valid Email.')    


