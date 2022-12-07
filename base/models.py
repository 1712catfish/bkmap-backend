from django.db import models
from django.contrib.auth.models import AbstractUser


class Post(models.Model):
    user = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    latlng = models.CharField(max_length=256)

class Task(models.Model):
    collector = models.CharField(max_length=256)
    janitor = models.CharField(max_length=256)
    vehicle = models.CharField(max_length=256)
    MCP = models.CharField(max_length=256)
