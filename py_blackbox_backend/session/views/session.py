from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from circuit.models import Circuit
from car.models import Car

from session.models import Session
from session.serializers.session import SessionSerializer


class SessionList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get(self, request, format=None):                
        query_params = self.request.query_params        
        filters = {k: v for k, v in query_params.items() if 
                   k in ['car_id', 'circuit_id', 'session_type_id']}
        sessions = Session.objects.filter(**filters)        
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
    lookup_field = "id"

