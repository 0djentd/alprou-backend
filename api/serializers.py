from rest_framework import serializers
from django.contrib.auth.models import User
from taggit.serializers import TagListSerializerField, TaggitSerializer
from core.models import Profile, Habit, Day


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["id", "url", "username",
                            "created", "modified", "user"]


class HabitSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    tags = TagListSerializerField()

    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ["id", "url", "created", "user",
                            "modified", "user", "completed", "completed_today"]


class DaySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Day
        fields = "__all__"
        read_only_fields = ["id", "url", "user", "habit", "datetime"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'profile', 'habits', 'days']
        read_only_fields = ["id", "url", 'profile', 'habits', 'days']
