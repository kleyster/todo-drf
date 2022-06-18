from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []


    objects = CustomUserManager()

    def __str__(self):
        return self.email