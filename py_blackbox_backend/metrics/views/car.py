from rest_framework.views import APIView
from rest_framework.response import Response

from session.models import Session, Stint, Lap
from circuit.models import Circuit

from session.serializers.lap import LapSerializer
from circuit.serializers.circuit import CircuitSerializer


class MetricsCarSummary(APIView):
    def get(self, request, car_id, format=None):
        summary = []
        circuits = Circuit.objects.all()

        for circuit in circuits:
            sessions = Session.objects.only(
                "id").filter(circuit_id=circuit.id,
                             user=request.user,
                             stint__id__isnull=False,
                             car__id=car_id).distinct()
            stints = Stint.objects.only('id').filter(
                session_id__in=sessions)

            laps = Lap.objects.filter(
                stint_id__in=stints).order_by("time")[:1000]

            if len(laps) > 0:
                best_lap = LapSerializer(laps[0]).data
            else:
                best_lap = {"time": None}

            summary.append({
                "circuit": CircuitSerializer(circuit).data,
                "lap": best_lap
            })

        return Response(summary)
