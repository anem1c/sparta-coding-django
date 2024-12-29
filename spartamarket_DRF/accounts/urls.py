from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

app_name = "accounts"

urlpatterns = [
    path("",views.CreateUserAPIView.as_view()),
    path("login/",TokenObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view()),
]
