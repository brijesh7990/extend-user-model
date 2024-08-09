from django.db import models
from django.contrib.auth.models import AbstractUser

from base.models import BaseModel
from .validator import validate_phone, validate_pincode
from .manager import CustomUserManager


# Create your models here.


class User(BaseModel, AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, unique=True, validators=[validate_phone])
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    pincode = models.CharField(max_length=6, blank=True, validators=[validate_pincode])

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username", "email", "password"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username
