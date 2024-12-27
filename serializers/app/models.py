from django.db import models

# Create your models here.

class Student(models.Model):
    Sid=models.IntegerField(primary_key=True)
    Sname=models.CharField(max_length=100)
    age=models.IntegerField()
    def __str__(self):
        return str(self.Sid)
    
class Teacher(models.Model):
    Tname=models.CharField(max_length=100)
    Sub=models.CharField(max_length=100)
    

    def __str__(self):
        return self.Tname
    