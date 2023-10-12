from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    bio = models.TextField(max_length=300, blank=True, null=True)