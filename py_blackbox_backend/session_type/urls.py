from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from session_type import views

urlpatterns = [
    path('', views.SessionTypeList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)