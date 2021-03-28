from circuit.models import Circuit
from circuit.serializers.circuit import CircuitSerializer
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from django.views.decorators.cache import cache_page


class CircuitList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer


class CircuitDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer
