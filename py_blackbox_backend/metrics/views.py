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
    def get(self, request, format=None):
        circuits = Circuit.objects.only("id").all()
        summary = []
        for circuit in circuits:
            sessions = Session.objects.only(
                "id").filter(circuit_id=circuit.id).all()

            stints = Stint.objects.only('id').filter(session_id__in=sessions)
            best_lap = Lap.objects.filter(
                stint_id__in=stints).order_by("-time").first()

            car = {"id": None, "name": None}

            best_time = None
            if best_lap:
                car = best_lap.stint_id.session_id.car

                best_time = best_lap.time
            summary.append(
                {"car": car, "circuit": circuit, "best_time": best_time})

        serializer = CircuitSummarySerializer(summary, many=True)
        return Response(serializer.data)
