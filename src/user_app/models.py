import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .manager import UserManager

# Create your models here.

class User(AbstractUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    

    def __str__(self):
        return self.email
    
