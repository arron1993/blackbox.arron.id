from rest_framework import serializers
from session_type.models import SessionType


class SessionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionType
        fields = ['id', 'name']