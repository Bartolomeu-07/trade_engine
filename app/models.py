from django.contrib.auth.models import AbstractUser
from django.db import models


class AssetType(models.Model):
    name = models.CharField(max_length=100)


class Asset(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    type = models.ForeignKey(AssetType, on_delete=models.CASCADE)


class Investor(AbstractUser):
    balance = models.FloatField()
    holdings = models.ManyToManyField(Asset, related_name='investors')
    is_admin = models.BooleanField(default=False)