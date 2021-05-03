from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from metrics.views.circuit import MetricsCircuitSummary
from metrics.views.car import MetricsCarSummary
from metrics.views.last_session import MetricLastSession

urlpatterns = [
    path('last-session/', MetricLastSession.as_view()),
    path('circuits/<str:car_group>/', MetricsCircuitSummary.as_view()),
    path('cars/<int:car_id>/', MetricsCarSummary.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
