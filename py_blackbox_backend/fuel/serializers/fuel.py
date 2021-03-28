from django.contrib.auth.models import User
from rest_framework import serializers


class FuelStatsSerializer(serializers.Serializer):
    median_lap_time = serializers.IntegerField(read_only=True)
    median_fuel_usage = serializers.FloatField(read_only=True)
