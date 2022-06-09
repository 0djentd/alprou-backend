from django.shortcuts import render
from rest_framework import generics, views, decorators, authentication
from django.contrib.auth.models import User
from . import serializers

class UsersAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class ProfilesListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ProfileSerializer