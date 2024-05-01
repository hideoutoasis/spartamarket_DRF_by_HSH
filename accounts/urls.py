from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", views.UserCreateAPIView.as_view(), name="sign_in"),
    path('api_auth/', include('rest_framework.urls')), # JWT가 제공하는 로그인 기능
    path("login/", views.LoginAPIView.as_view(), name="log_in"), # 내가 만든 로그인 기능
    path("<str:username>/", views.ProfileDetailAPIView.as_view(), name="profile_detail"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
