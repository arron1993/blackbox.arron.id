from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/circuits/', include('circuit.urls')),
    path('api/cars/', include('car.urls')),
    path('api/session/', include('session.urls')),
    path('api/types/', include('session_type.urls')),
    path('api/fuel/', include('fuel.urls')),
    path('api/metrics/', include('metrics.urls')),
    path('api/signin/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/signin/refresh/',
         jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
