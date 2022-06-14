from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
import rest_framework
from . import views

urlpatterns = [
        path("profiles/", views.ProfilesListCreateAPIView.as_view(), name='profiles-list'),
        path("profiles/<int:pk>", views.ProfileDetailsAPIView.as_view(), name='profile-list'),
        path("habits/", views.HabitsListCreateAPIView.as_view(), name='habits-list'),
        path("habits/<int:pk>", views.HabitDetailsAPIView.as_view(), name='habit-detail'),
        # path("profiles/<int:pk>/", views.ProfileDetailsAPIView.as_view()),
        path("", include("rest_framework.urls")),
        path("authtoken/", obtain_auth_token),
            ]