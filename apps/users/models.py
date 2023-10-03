from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.users.managers import UserManager

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()