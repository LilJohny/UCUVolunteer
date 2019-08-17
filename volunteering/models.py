from django.db import models
from django.contrib.auth.models import User
from account.models import Profile
import datetime


class Event(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)