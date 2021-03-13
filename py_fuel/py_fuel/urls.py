from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', include('circuit.urls')),
    path('api/signin/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/signin/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]