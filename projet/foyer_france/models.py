from django.db import models
import time


class Product(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    price = models.IntegerField(default=0)


class HouseHold(models.Model):
    managerName = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    phoneNumber = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(default="", max_length=100)
    postalCode = models.CharField(max_length=100)
    totalMembers = models.IntegerField(default=0)
    products = models.ManyToManyField(
        Product,
        through='Command'
    )


class Command(models.Model):
    houseHold = models.ForeignKey(HouseHold, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    dateOfCommand = models.DecimalField(default=time.time(), max_digits=20, decimal_places=10)
