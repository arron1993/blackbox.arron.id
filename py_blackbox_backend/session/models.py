from django.db import models
from django.contrib.auth.models import User

from circuit.models import Circuit
from car.models import Car
from session_type.models import SessionType


class Session(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    circuit = models.ForeignKey(Circuit, on_delete=models.DO_NOTHING)
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    session_type = models.ForeignKey(SessionType, on_delete=models.DO_NOTHING)

    session_length = models.IntegerField()


class Stint(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)


class Lap(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stint_id = models.ForeignKey(Stint, on_delete=models.CASCADE)
    number = models.IntegerField()
    time = models.IntegerField()
    delta_time = models.IntegerField()
    fuel_used = models.FloatField()
    position = models.IntegerField()
    is_valid = models.BooleanField()

    sector1 = models.IntegerField(null=True)
    sector2 = models.IntegerField(null=True)
    sector3 = models.IntegerField(null=True)

    num_cars = models.IntegerField()
