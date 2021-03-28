import statistics

from rest_framework.response import Response
from rest_framework.views import APIView

from session.models import Session, Stint, Lap
from fuel.serializers.fuel import FuelStatsSerializer


class FuelStatsView(APIView):

    def get(self, request, car_id, circuit_id, format=None):

        # use the last 100 sessions
        sessions = Session.objects.only("id").filter(
            car_id=car_id,
            circuit_id=circuit_id,
            user_id=request.user.id).order_by("-created_at")[:100]

        if len(sessions) == 0:
            return Response({})
        stints = Stint.objects.only('id').filter(session_id__in=sessions)
        laps = Lap.objects.filter(stint_id__in=stints)

        lap_times = []
        fuel_usage = []
        for lap in laps:
            lap_times.append(lap.time)
            fuel_usage.append(lap.fuel_used)
        fuel_stats = {
            'median_lap_time': statistics.median(lap_times),
            'median_fuel_usage': statistics.median(fuel_usage)
        }
        serializer = FuelStatsSerializer(fuel_stats)
        return Response(serializer.data)
