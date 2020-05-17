from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,auth
# Create your models here.
class UserRegister(models.Model):
    username = models.EmailField(max_length=254)
    name = models.CharField(max_length=100)
    housenumber = models.IntegerField()
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.IntegerField()
    mobile = models.BigIntegerField()
    usertype = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name    


class CollectRegister1(models.Model):
    username = models.EmailField(max_length=254)
    cname = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.IntegerField()
    mobile = models.BigIntegerField()
    status = models.CharField(max_length=100)
    
    

    

    def __str__(self):
        return self.cname    




class Sell(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    cname = models.CharField(max_length=100)
    wastetype = models.CharField(max_length=100)
    weight = models.FloatField(max_length=100)
    # quantity = models.FloatField(max_length=100)
    price = models.FloatField(max_length=100)
    status = models.CharField(max_length=100)
    # date = models.DateTimeField()

    def __str__(self):
        return self.wastetype




