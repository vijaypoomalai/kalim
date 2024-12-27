from django.db import models

# Create your models here.

class Student(models.Model):
    Sno=models.IntegerField()
    Sname=models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    result = models.CharField(max_length=20,choices= [('P','Pass'),('F','Fail')] )
    passby=models.CharField(max_length=50,default='')

    def __str__(self):
        return self.Sname