from django.db import models
from django.contrib.auth.models import AbstractUser


class Post(models.Model):
    latlng = models.CharField(max_length=256)
    text = models.CharField(max_length=256)


