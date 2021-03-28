from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from session.views import session, lap, stint

urlpatterns = [
    path('', session.SessionList.as_view()),
    path('<int:id>/', session.SessionDetail.as_view()),

    path('<int:session_id>/stints/', stint.StintList.as_view()),
    path('<int:session_id>/stints/<int:id>/', stint.StintDetail.as_view()),

    path('<int:session_id>/stints/<int:id>/laps/', lap.LapList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
