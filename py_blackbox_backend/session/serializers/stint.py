from rest_framework import serializers
from session.models import Stint

from session.serializers.lap import LapSerializer


class StintSerializer(serializers.ModelSerializer):
    laps = LapSerializer(many=True, read_only=True, source='lap_set')

    class Meta:
        model = Stint
        fields = ['id', 'session_id', 'laps']
