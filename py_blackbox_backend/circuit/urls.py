from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from circuit import views

urlpatterns = [
    path('', views.CircuitList.as_view()),
    path('<int:pk>/', views.CircuitDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)