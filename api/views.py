from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from core.models import Habit
from core.serializers import HabitSerializer


class HabitAPIViewSet(ViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
