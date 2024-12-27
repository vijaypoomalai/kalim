from django.db import models

# Create your models here.

class Student(models.Model):
    Sno=models.IntegerField()
    Sname=models.CharField(max_length=50)

    def __str__(self):
        return self.Sname