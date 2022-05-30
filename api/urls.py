from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
import rest_framework

urlpatterns = [
        path("", include("rest_framework.urls")),
        path("authtoken/", obtain_auth_token),
            ]
