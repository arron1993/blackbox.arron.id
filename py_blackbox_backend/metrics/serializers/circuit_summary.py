from rest_framework import serializers

from car.serializers.car import CarSerializer
from session.serializers.lap import LapSerializer
from circuit.serializers.circuit import CircuitSerializer


class CircuitSummarySerializer(serializers.Serializer):
    best_time = serializers.IntegerField()
    median_time = serializers.IntegerField()
    session_id = serializers.IntegerField()
    total_laps = serializers.IntegerField()
    total_sessions = serializers.IntegerField()
    new_best = serializers.BooleanField()
    car = CarSerializer()
    circuit = CircuitSerializer()
