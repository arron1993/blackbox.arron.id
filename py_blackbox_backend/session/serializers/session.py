from rest_framework import serializers
from session.models import Session, Lap
from car.models import Car
from circuit.models import Circuit

from circuit.serializers.circuit import CircuitSerializer

from session.serializers.stint import StintSerializer

from session_type.models import SessionType
from session_type.serializers.session_type import SessionTypeSerializer

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

    session_type = SessionTypeSerializer(read_only=True)
    session_type_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source='session_type',
        queryset=SessionType.objects.all()
    )

    stints = StintSerializer(many=True, read_only=True, source='stint_set')

    class Meta:
        model = Session
        fields = [
            'id', 'user',
            'car', "car_id",
            'circuit', 'circuit_id',
            "session_type", "session_type_id",
            "created_at", "stints"
        ]


class SessionListSerializer(SessionSerializer):
    class Meta:
        model = Session
        fields = [
            'id', 'user',
            'car', "car_id",
            'circuit', 'circuit_id',
            "session_type", "session_type_id",
            "created_at"
        ]
