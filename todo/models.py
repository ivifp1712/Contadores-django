from email.policy import default
from enum import unique
from random import choice as ch
from typing import Any
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, default=f"{''.join([ch('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+') for i in range(6)])}", unique=True)
    dia = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    fcompleted = models.IntegerField(default=0)
    creador = models.CharField(max_length=100, default="Diosito")
    contra= models.CharField(max_length=100, default="ivi")
    private = models.BooleanField(default=False)
    def __str__(self):
        return self.title
        