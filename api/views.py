import logging

from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAdminUser

from core.models import Profile, Habit

from . import serializers
from . mixins import IsObjectAuthorPermission


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ProfilesViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


class HabitsViewset(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = serializers.HabitSerializer
