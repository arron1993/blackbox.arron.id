from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from circuit.models import Circuit
from circuit.serializers.circuit import CircuitSerializer


class CircuitList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer

    @method_decorator(cache_page(60*60*24))
    def list(self, request):
        queryset = self.get_queryset()
        serializer = CircuitSerializer(queryset, many=True)
        return Response(serializer.data)


class CircuitDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer
