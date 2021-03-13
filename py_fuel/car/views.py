from car.models import Car
from car.serializers.car import CarSerializer
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated


class CarList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer