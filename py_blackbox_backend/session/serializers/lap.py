from rest_framework import serializers
from session.models import Lap


class LapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lap
        fields = [
            'id', 'stint_id', 'number', 'time', 'fuel_used',
            'delta_time', 'position', 'is_valid', 'sector1',
            'sector2', 'sector3', 'num_cars',
            'front_left_pressure', "front_right_pressure",
            "rear_left_pressure", "rear_right_pressure",
            "track_temp", "air_temp"
        ]
