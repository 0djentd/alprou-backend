import logging

from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAdminUser

from core.models import Profile, Habit

from . import serializers
from . permissions import IsObjectAuthorPermission, IsObjectPublic


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ProfilesViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsObjectPublic, IsObjectAuthorPermission, IsAdminUser]


class HabitsViewset(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = serializers.HabitSerializer
    permission_classes = [IsObjectPublic, IsObjectAuthorPermission, IsAdminUser]