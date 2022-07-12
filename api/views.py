import logging

from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action, api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from core.models import Profile
from core.serializers import ProfileSerializer, UserSerializer

from habits.models import Habit, Day
from habits.serializers import HabitSerializer, DaySerializer

from .mixins import VisibleToUserObjectsMixin
from .permissions import IsSameIdAsUser


logger = logging.getLogger(__name__)


class HabitsViewset(VisibleToUserObjectsMixin, viewsets.ModelViewSet):
    model = Habit
    serializer_class = HabitSerializer
    filterset_fields = ["user"]
    search_fields = [
        "user",
        "name",
        "description",
        "days",
        "created",
        "modified",
        "tags",
    ]

    @action(methods=["PATCH"], detail=True)
    def done(self, request, pk):
        instance = get_object_or_404(self.model, id=pk)
        if instance.user != request.user:
            return HttpResponseForbidden()
        instance.done()
        instance.save()
        return Response({}, status=201)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DaysViewset(
        VisibleToUserObjectsMixin,
        viewsets.generics.RetrieveDestroyAPIView,
        viewsets.generics.ListAPIView,
        viewsets.GenericViewSet):
    model = Day
    serializer_class = DaySerializer


class UserAPIView(APIView):
    """Returns currently active user."""
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request) -> UserSerializer:
        data = UserSerializer(request.user, context={'request': request}).data
        return Response(data)


class ProfilesViewset(
        VisibleToUserObjectsMixin,
        viewsets.generics.RetrieveUpdateAPIView,
        viewsets.generics.ListAPIView,
        viewsets.GenericViewSet):
    model = Profile
    serializer_class = ProfileSerializer

    @action(methods=["GET"], detail=False)
    def active(self, request):
        """Returns currently active profile"""
        profile = request.user.profile
        data = ProfileSerializer(profile, context={"request": request}).data
        return Response(data)
