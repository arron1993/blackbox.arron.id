from rest_framework import serializers
from session.models import Session, Lap
from car.models import Car
from circuit.models import Circuit
from circuit.serializers.circuit import CircuitSerializer

from session.serializers.stint import StintSerializer

from car.serializers.car import CarSerializer


class SessionSerializer(serializers.ModelSerializer):

    car = CarSerializer(read_only=True)
    car_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source='car',
        queryset=Car.objects.all()
    )

    circuit = CircuitSerializer(read_only=True)
    circuit_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source='circuit',
        queryset=Circuit.objects.all()
    )

    stints = StintSerializer(many=True, read_only=True, source='stint_set')

    class Meta:
        model = Session
        fields = [
            'id', 'user', 'type',
            'car', 'circuit', 'circuit_id',
            "car_id", "created_at", "stints"]





