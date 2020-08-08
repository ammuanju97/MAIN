from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,auth
# Create your models here.




class AddProduct(models.Model):
    user = models.CharField(max_length=100)
    productname = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.productname

class CollectDetails(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cname = models.CharField(max_length=100)
    wastetype = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.username


class BookForm(models.Model):
    tokenno = models.CharField(max_length=100)
    cname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    wastetype = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.cname

class Payment(models.Model):
    cardnumber = models.IntegerField()
    expirydate = models.DateField()
    cvv = models.IntegerField()
    nameofcard = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nameofcard

class SellPayment(models.Model):
    cardnumber = models.IntegerField()
    expirydate = models.DateField()
    cvv = models.IntegerField()
    nameofcard = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nameofcard