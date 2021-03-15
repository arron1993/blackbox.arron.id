from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from session.models import Stint
from session.serializers.stint import StintSerializer


class StintList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = StintSerializer
    queryset = Stint.objects.all()

    def get(self, request, **kwargs):
        session_id = kwargs.get("session_id")
        stints = Stint.objects.filter(session_id=session_id)
        serializer = StintSerializer(stints, many=True)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        stint = request.data
        stint["session_id"] = kwargs.get("session_id")
        serializer = StintSerializer(data=stint)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StintDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Stint.objects.all()
    serializer_class = StintSerializer
    lookup_field = "id"