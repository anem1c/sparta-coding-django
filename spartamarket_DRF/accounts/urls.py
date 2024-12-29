from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("",views.CreateUserAPIView.as_view()),
    path("login/",views.AccountsLoginAPIView.as_view())
]
