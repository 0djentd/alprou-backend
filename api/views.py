import logging

from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from core.models import Profile, Habit, Day

from . import serializers
from . mixins import VisibleObjectsMixin
from . permissions import IsSameIdAsUser


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ProfilesViewset(VisibleObjectsMixin, viewsets.ModelViewSet):
    model = Profile
    serializer_class = serializers.ProfileSerializer


class HabitsViewset(VisibleObjectsMixin, viewsets.ModelViewSet):
    model = Habit
    serializer_class = serializers.HabitSerializer


class DaysViewset(VisibleObjectsMixin, viewsets.ModelViewSet):
    model = Day
    serializer_class = serializers.DaySerializer


class UsersViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated & IsSameIdAsUser]

    def get_queryset(self) -> QuerySet:
        queryset = User.objects.all().filter(id=self.request.user.id)
        return queryset
