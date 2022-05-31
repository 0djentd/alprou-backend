from rest_framework.serializers import ModelSerializer
from .models import Habit


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        exclude = ['']
