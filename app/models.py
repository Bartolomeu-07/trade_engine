from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey
from decimal import Decimal


class AssetType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=3, max_digits=10)
    type = models.ForeignKey(AssetType, on_delete=models.CASCADE)


class Investor(AbstractUser):
    balance = models.DecimalField(default=100000, decimal_places=3, max_digits=10)


class Holding(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


class Order(models.Model):
    BUY = "BUY"
    SELL = "SELL"
    SIDE_CHOICES = [(BUY, "Buy"), (SELL, "Sell")]

    id = models.AutoField(primary_key=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    investor = ForeignKey(Investor, on_delete=models.CASCADE)
    side = models.CharField(max_length=4, choices=SIDE_CHOICES)
    datetime = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(editable=False, decimal_places=3, max_digits=10)

    def save(self, *args, **kwargs):
        self.value = self.asset.price * self.quantity
        super().save(*args, **kwargs)
