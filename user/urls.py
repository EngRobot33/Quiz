from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserView, UserUpdateView, UserChangePasswordView, RegisterView


app_name = 'user'

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('info/', UserView.as_view(), name='user'),
    path('update/', UserUpdateView.as_view(), name='user-update'),
    path('change-password/', UserChangePasswordView.as_view(), name='user-change-password'),
]