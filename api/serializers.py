from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile, Habit, Day


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "url", "user", "public", "public_username", "profile_image", "background_image"]
        read_only_fields = ["id", "url", "user"]


class HabitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Habit
        fields = ["id", "url", "name", "description", "user",
                  "active", "negative", "public", "completed"]
        read_only_fields = ["id", "url", "user", "completed"]


class DaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Day
        fields = ["id", "url", "user", "habit", "datetime", "public"]
        read_only_fields = ["id", "url", "user", "habit", "datetime"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'profile', 'habits', 'days']
        read_only_fields = ["id", "url", 'profile', 'habits', 'days']
