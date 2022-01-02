from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from SocaProject import settings


class OtherDetails(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    no_team = models.CharField(max_length=1000,default='NO TEAM')

def __str__(self):
    return self.user
