from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.


class CustomerUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100, unique=True)
    user_bio = models.CharField(max_length=200, blank=True)
    user_profile_image = models.ImageField(upload_to="profile", blank=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = UserManager()
