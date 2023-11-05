from django.core.checks import messages
from django.db import models
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render


# Create your models here.
class UserRegister(models.Model):
    user_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    password1=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)
    def __str__(self):
        return self.user_name





