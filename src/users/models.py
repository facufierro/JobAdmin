from django.db import models
from django.contrib.auth.models import AbstractUser


class custom_user(AbstractUser):
    address = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
