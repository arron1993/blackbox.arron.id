import statistics

from django.db.models import Min

from rest_framework.views import APIView
from rest_framework.response import Response

from session.models import Session, Stint, Lap
from circuit.models import Circuit

from session.serializers.session import SessionSerializer
from metrics.serializers.circuit_summary import CircuitSummarySerializer


class MetricLastSession(APIView):

    def get(self, request, format=None):
        last_session = Session.objects.filter(
            user=request.user).order_by("-created_at").first()
        serializer = SessionSerializer(last_session)
        return Response(serializer.data)


class MetricsCircuitSummary(APIView):
    def get(self, request, car_group='gt3', format=None):
        circuits = Circuit.objects.only("id").all()
        summary = []
        for circuit in circuits:
            sessions = Session.objects.only(
                "id").filter(circuit_id=circuit.id,
                             user=request.user,
                             stint__id__isnull=False,
                             car__group=car_group).distinct()

            stints = Stint.objects.only('id').filter(
                session_id__in=sessions)
            laps = Lap.objects.filter(
                stint_id__in=stints).order_by("time")

            median_time = None
            car = {"name": None, "id": None}
            best_time = None
            session_id = None
            best_lap = None
            if len(laps) > 0:
                best_lap = laps[0]
                median_time = statistics.median([lap.time for lap in laps])
                car = best_lap.stint_id.session_id.car
                best_time = best_lap.time
                session_id = best_lap.stint_id.session_id.id

            summary.append({
                "car": car,
                "circuit": circuit,
                "session_id": session_id,
                "best_time": best_time,
                "median_time": median_time})

        serializer = CircuitSummarySerializer(summary, many=True)
        return Response(serializer.data)
