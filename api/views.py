import logging

from rest_framework import viewsets

from core.models import Profile, Habit

from . import serializers
from . mixins import VisibleObjectsMixin


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ProfilesViewset(VisibleObjectsMixin, viewsets.ModelViewSet):
    model = Profile
    serializer_class = serializers.ProfileSerializer


class HabitsViewset(VisibleObjectsMixin, viewsets.ModelViewSet):
    model = Habit
    serializer_class = serializers.HabitSerializer
