import logging

from rest_framework import generics, mixins
from rest_framework.permissions import IsAdminUser

from core.models import Profile, Habit

from . import serializers
from . mixins import IsObjectAuthorPermission


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ProfilesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


class ProfileDetailsAPIView(# IsObjectAuthorPermission,
                            generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


class HabitsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = serializers.HabitSerializer


class HabitDetailsAPIView(# IsObjectAuthorPermission,
                            generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = serializers.HabitSerializer
