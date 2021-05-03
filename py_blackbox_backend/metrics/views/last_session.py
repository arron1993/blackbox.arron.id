from rest_framework.views import APIView
from rest_framework.response import Response

from session.models import Session
from session.serializers.session import SessionSerializer


class MetricLastSession(APIView):

    def get(self, request, format=None):
        last_session = Session.objects.filter(
            user=request.user).order_by("-created_at").first()
        serializer = SessionSerializer(last_session)
        return Response(serializer.data)
