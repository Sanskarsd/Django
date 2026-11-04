from django.db import models
import datetime

# Create your models here.


class Student(models.Model):
    roll = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    city = models.CharField(max_length=100)
