from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from metrics import views

urlpatterns = [
    path('last-session/', views.MetricLastSession.as_view()),
    path('circuits/<str:car_group>/', views.MetricsCircuitSummary.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
