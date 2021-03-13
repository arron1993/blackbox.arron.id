from django.db import models

class Circuit(models.Model):
    name = models.CharField(max_length=100)
    keyname = models.CharField(max_length=100)