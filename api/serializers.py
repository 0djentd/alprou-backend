from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "profile"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ["user"]