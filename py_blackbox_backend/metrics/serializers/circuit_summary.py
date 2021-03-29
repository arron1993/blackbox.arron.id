from rest_framework import serializers

from car.serializers.car import CarSerializer
from circuit.serializers.circuit import CircuitSerializer


class CircuitSummarySerializer(serializers.Serializer):
    best_time = serializers.IntegerField()
    session_id = serializers.IntegerField()
    car = CarSerializer()
    circuit = CircuitSerializer()
