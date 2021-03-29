from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=100)
    keyname = models.CharField(max_length=100)
    group = models.CharField(max_length=10)
