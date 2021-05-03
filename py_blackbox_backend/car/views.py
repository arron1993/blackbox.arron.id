from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from car.models import Car
from car.serializers.car import CarSerializer


class CarList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    @method_decorator(cache_page(60*60*24))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)


class CarDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer
