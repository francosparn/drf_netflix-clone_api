from django.urls import path

from apps.users.api.views import RegisterAPIView, UserAPIView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('auth/register', RegisterAPIView.as_view()),
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me', UserAPIView.as_view())
]