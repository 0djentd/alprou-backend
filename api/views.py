import logging

from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAdminUser

from core.models import Profile, Habit

from . import serializers
from . permissions import IsObjectAuthorPermission, IsObjectPublic


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ProfilesViewset(viewsets.ModelViewSet):
    model = Profile
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsObjectPublic, IsObjectAuthorPermission, IsAdminUser]

    def get_queryset(self):
        queryset_public = self.model.objects.all().filter(public=True)
        queryset_user = self.model.objects.all().filter(user=self.request.user)
        return queryset_public | queryset_user

class HabitsViewset(viewsets.ModelViewSet):
    model = Habit
    serializer_class = serializers.HabitSerializer
    permission_classes = [IsObjectPublic, IsObjectAuthorPermission, IsAdminUser]

    def get_queryset(self):
        queryset_public = self.model.objects.all().filter(public=True)
        queryset_user = self.model.objects.all().filter(user=self.request.user)
        return queryset_public | queryset_user
