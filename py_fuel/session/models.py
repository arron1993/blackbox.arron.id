from django.db import models
from django.contrib.auth.models import User

from circuit.models import Circuit
from car.models import Car

class Session(models.Model):
    type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)    
    circuit = models.ForeignKey(Circuit, on_delete=models.DO_NOTHING)
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING )


class Lap(models.Model):
    number = models.IntegerField()
    time = models.IntegerField()
    session = models.ForeignKey(Session, on_delete=models.CASCADE)