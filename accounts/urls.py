from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", TokenObtainPairView.as_view(), name="sign_in"),
    path("login/", TokenObtainPairView.as_view(), name="log_in"),
    path("<str:username>/", views.ProfileDetailAPIView.as_view(), name="profile_detail"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
