from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from SocaProject import settings


class CustomUser(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.ForeignKey(User,on_delete=models.CASCADE)
    fave_team= models.CharField(max_length=1000)

def __str__(self):
    return self.email
