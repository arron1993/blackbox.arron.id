from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from session_type.models import SessionType
from session_type.serializers.session_type import SessionTypeSerializer


class SessionTypeList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SessionTypeSerializer
    queryset = SessionType.objects.all()

    @method_decorator(cache_page(60*60*24))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = SessionTypeSerializer(queryset, many=True)
        return Response(serializer.data)
