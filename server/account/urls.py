from .views import *
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify', TokenVerifyView.as_view(), name='token_verify'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='log_out'),
    path('nickname', NameVerifyView.as_view(), name='nickname'),
    path('user', UserView.as_view(), name='user')
]
