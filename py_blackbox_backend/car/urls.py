from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from car import views

urlpatterns = [
    path('', views.CarList.as_view()),
    path('<int:pk>/', views.CarDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
