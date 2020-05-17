from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,auth

# Create your models here.
class AddCategory(models.Model):
    categoryname = models.CharField(max_length=100)
 

    def __str__(self):
        return self.categoryname

class AddRecycle(models.Model):
    categoryname = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryname