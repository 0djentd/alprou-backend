import logging
import json

from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Profile, Habit, Day

from . import serializers
from . mixins import VisibleObjectsMixin
from . permissions import IsSameIdAsUser


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ProfilesViewset(VisibleObjectsMixin, viewsets.ModelViewSet):
    model = Profile
    serializer_class = serializers.ProfileSerializer

    @action(methods=['GET'], detail=False)
    def get_user_profile_id(self, request):
        pk = request.user.profile.id
        return Response({"pk": pk})


class HabitsViewset(VisibleObjectsMixin, viewsets.ModelViewSet):
    model = Habit
    serializer_class = serializers.HabitSerializer
    filterset_fields = ("active", "negative", "user", "public")
    search_fields = ["user", 'name', 'description',
                     'days', 'created', 'modified', 'tags']

    @action(methods=['PATCH'], detail=True)
    def done(self, request, pk):
        instance = get_object_or_404(self.model, id=pk)
        if instance.user != request.user:
            return HttpResponseForbidden()
        instance.done()
        instance.save()
        return Response({}, status=201)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DaysViewset(VisibleObjectsMixin, viewsets.ModelViewSet):
    model = Day
    serializer_class = serializers.DaySerializer


class UsersViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated & IsSameIdAsUser]

    def get_queryset(self) -> QuerySet:
        queryset = User.objects.all().filter(id=self.request.user.id)
        return queryset

    @action(methods=['GET'], detail=False)
    def get_user_id(self, request):
        pk = request.user.id
        return Response({"pk": pk})
