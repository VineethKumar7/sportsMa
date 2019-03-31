from django.db import models
from .choises import *

# Create your models here.
class Login(models.Model):
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=50)
    user_role = models.CharField(max_length=10)
    status = models.IntegerField(default=1)
    login_id = models.IntegerField(default=0)

class Users(models.Model):
    firstname = models.CharField(max_length=35)
    middlename = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    mobile = models.IntegerField()
    location = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    login = models.ForeignKey(Login, on_delete=models.CASCADE)

class Player(models.Model):
    firstname = models.CharField(max_length=35)
    middlename = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    eventname = models.CharField(max_length=30, default="None", choices = EVENT_CHOICES)
    def __str__(self):
        return self.firstname

class Tournament(models.Model):
    eventname = models.CharField(max_length=30, default="None", choices = EVENT_CHOICES)
    venue = models.CharField(max_length=30)
    date = models.DateField(max_length=30)
    time = models.TimeField(max_length=30)

class Awards(models.Model):
    eventname = models.CharField(max_length=30, default="None", choices = EVENT_CHOICES)
    first = models.CharField(max_length=30)
    second = models.CharField(max_length=30)
    third = models.CharField(max_length=30)
