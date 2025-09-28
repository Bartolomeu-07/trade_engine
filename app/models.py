from django.contrib.auth.models import AbstractUser
from django.db import models


class AssetType(models.Model):
    name = models.CharField(max_length=100)