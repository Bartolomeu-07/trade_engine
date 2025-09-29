from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey


class AssetType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    type = models.ForeignKey(AssetType, on_delete=models.CASCADE)


class Investor(AbstractUser):
    balance = models.FloatField()
    holdings = models.ManyToManyField(Asset, related_name='investors')


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    investor = ForeignKey(Investor, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    value = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        self.value = self.asset.price * self.quantity
        super().save(*args, **kwargs)
