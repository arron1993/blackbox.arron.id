from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from session.models import Lap
from session.serializers.lap import LapSerializer


class LapList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = LapSerializer
    queryset = Lap.objects.all()

    def get(self, request, **kwargs):
        session_id = kwargs.get("session_id")
        laps = Lap.objects.filter(session_id=session_id)
        serializer = LapSerializer(laps, many=True)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        lap = request.data
        lap["stint_id"] = kwargs.get("id")
        serializer = LapSerializer(data=lap)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
