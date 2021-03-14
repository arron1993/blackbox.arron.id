from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from session import views

urlpatterns = [
    path('', views.SessionList.as_view()),
    path('<int:pk>/', views.SessionDetail.as_view()),
    path('<int:pk>/laps/', views.LapList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)