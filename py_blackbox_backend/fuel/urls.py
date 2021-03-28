from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from fuel import views

urlpatterns = [
    path('<int:car_id>/<int:circuit_id>/', views.FuelStatsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
