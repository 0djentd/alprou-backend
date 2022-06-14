from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile, Habit


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = []


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        exclude = []
