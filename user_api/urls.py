from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView

urlpatterns = [
    path('login/',obtain_auth_token, name="login"),
    path('register/',RegisterView.as_view(), name="register"),

    
]