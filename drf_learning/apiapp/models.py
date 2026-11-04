from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Profile(AbstractUser):
    email = models.EmailField()
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    REQUIRED_FIELDS = ["email", "age", "city"]
