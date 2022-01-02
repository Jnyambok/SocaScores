from django.contrib import admin
from .models import OtherDetails
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.register(OtherDetails)