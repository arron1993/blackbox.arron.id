from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from session_type.models import SessionType
from session_type.serializers.session_type import SessionTypeSerializer


class SessionTypeList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SessionTypeSerializer
    queryset = SessionType.objects.all()