from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    address = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, blank=True)
