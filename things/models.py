from pickle import TRUE
from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    quantity = models.PositiveIntegerField(MaxValueValidator(100), unique=TRUE)
