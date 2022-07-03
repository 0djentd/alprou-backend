from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Habit, Day


class HabitSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    completed_today = serializers.BooleanField(read_only=True)
    tags = TagListSerializerField()

    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = [
            "id",
            "url",
            "created",
            "user",
            "modified",
            "user",
            "completed",
            "completed_today",
        ]


class DaySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Day
        fields = "__all__"
        read_only_fields = ["id", "url", "user", "habit", "datetime"]
