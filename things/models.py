from pickle import TRUE
from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Thing(models.Model):
    name = models.CharField(blank=False,max_length=30,unique=False)
    description = models.CharField(max_length=120,unique=False,blank=True)
    quantity = models.PositiveIntegerField(MaxValueValidator(100), unique=True)
