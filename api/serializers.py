from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile, Habit


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user']


class HabitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Habit
        exclude = ['user']