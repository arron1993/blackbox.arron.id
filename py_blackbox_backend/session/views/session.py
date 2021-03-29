from rest_framework import generics, status, filters
from rest_framework.views import APIView
from py_blackbox_backend.pagination import PageNumberOnlyPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from circuit.models import Circuit
from car.models import Car

from session.models import Session
from session.serializers.session import SessionSerializer, SessionListSerializer

from session_type.models import SessionType
from session.permissions import IsOwner


class SessionList(APIView, PageNumberOnlyPagination):
    permission_classes = (IsAuthenticated,)
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    page_size = 20

    def get(self, request, format=None):
        query_params = self.request.query_params
        filters = {k: v for k, v in query_params.items() if
                   k in ['car_id', 'circuit_id', 'session_type_id']}
        filters["user_id"] = request.user.id
        sessions = Session.objects.filter(**filters).order_by("-created_at")

        results = self.paginate_queryset(sessions, request, view=self)

        serializer = SessionListSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        session = request.data
        session["user"] = request.user.id
        session["circuit_id"] = Circuit.objects.get(
            keyname=session['circuit']).id
        session["car_id"] = Car.objects.get(keyname=session['car']).id
        session["session_type_id"] = SessionType.objects.get(
            key=session['session_type']).id
        serializer = SessionSerializer(data=session)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner, )
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    lookup_field = "id"
