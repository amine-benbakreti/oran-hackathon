from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    description=models.TextField(max_length=499,blank=True,default='')

    def __str__(self):
        return self.username
