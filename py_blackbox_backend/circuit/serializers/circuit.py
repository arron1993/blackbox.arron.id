from rest_framework import serializers
from circuit.models import Circuit


class CircuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuit
        fields = ['id', 'name', 'keyname']