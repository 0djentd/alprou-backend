from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile, Habit, Day


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        exclude = []


class HabitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Habit
        fields = ["id", "url", "name", "description", "user",
                  "active", "negative", "public", "completed"]


class DaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Day
        exclude = []


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'habits']
        read_only_fields = ['habits']
