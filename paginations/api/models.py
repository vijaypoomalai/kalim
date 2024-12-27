from django.db import models

# Create your models here.

class Student(models.Model):
    Sname=models.CharField(max_length=50)
    Sno=models.IntegerField()

    def __str__(self):
        return str(self.id)