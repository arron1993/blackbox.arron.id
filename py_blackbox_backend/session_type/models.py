from django.db import models


class SessionType(models.Model):
    name = models.CharField(max_length=50)
    key = models.IntegerField()
