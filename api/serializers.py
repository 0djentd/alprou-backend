from rest_framework import serializers
from django.contrib.auth.models import User
from taggit.serializers import TagListSerializerField, TaggitSerializer
from core.models import Profile, Habit, Day


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "url", "user", "created", "modified", "public", "public_username", "profile_image", "background_image"]
        read_only_fields = ["id", "url", "created", "modified", "user"]


class HabitSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Habit
        fields = ["id", "url", "created", "modified", "name", "description", "user",
                  "active", "negative", "public", "completed", "tags"]
        read_only_fields = ["id", "url", "created", "modified", "user", "completed"]


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
