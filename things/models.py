from pickle import TRUE
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
# Create your models here.

class Thing(models.Model):
    name = models.CharField(blank=False,max_length=30,unique=True)
    description = models.CharField(max_length=120,unique=False,blank=True)
    quantity = models.PositiveIntegerField(validators=([MinValueValidator(0),MaxValueValidator(100)]), unique=False)
