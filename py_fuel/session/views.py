from session.models import Session, Lap
from circuit.models import Circuit
from car.models import Car
from session.serializers.session import (SessionSerializer, LapSerializer)

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class SessionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get(self, request, format=None):
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        session = request.data
        session["user"] = request.user.id
        session["circuit_id"] = Circuit.objects.get(keyname=session['circuit']).id
        session["car_id"] = Car.objects.get(keyname=session['car']).id

        serializer = SessionSerializer(data=session)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Session.objects.all()
    serializer_class = SessionSerializer



class LapList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = LapSerializer
    queryset = Session.objects.all()

    def get(self, request, **kwargs):
        session_id = kwargs.get("pk")
        laps = Lap.objects.filter(session_id=session_id)
        serializer = LapSerializer(laps, many=True)
        return Response(serializer.data)

    
    def post(self, request, **kwargs):
        lap = request.data
        lap["session_id"] = kwargs.get("pk")

        serializer = LapSerializer(data=lap)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)