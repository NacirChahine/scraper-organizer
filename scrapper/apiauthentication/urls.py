from django.urls import path, include
from .views import RegisterUserAPIView, ChangePasswordView, ProfileView, UpdateProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('signup', RegisterUserAPIView.as_view(), name='signup'),
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('profile-get', ProfileView.as_view(), name='profile'),
    path('change-password', ChangePasswordView.as_view(), name='change_password'),
    path('update-profile/<int:pk>', UpdateProfileView.as_view(), name='auth_update_profile'),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # /login/ /logout/
    path('refreshToken', TokenRefreshView.as_view(), name='refresh_token'),
    path('verifyToken', TokenVerifyView.as_view(), name='verify_token'),
]
