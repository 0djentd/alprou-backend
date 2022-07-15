import logging

from django.contrib.auth.models import User
from django.db.models import QuerySet

from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsObjectAuthorOrReadonlyIfVisible

from core.models import Profile
from core.serializers import ProfileSerializer, UserSerializer

from habits.models import Habit, Day
from habits.serializers import HabitSerializer, DaySerializer

from .mixins import VisibleModelAPIViewsetMixin


logger = logging.getLogger(__name__)


class HabitsViewset(VisibleModelAPIViewsetMixin, viewsets.ModelViewSet):
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
        VisibleModelAPIViewsetMixin,
        viewsets.generics.RetrieveDestroyAPIView,
        viewsets.generics.ListAPIView,
        viewsets.GenericViewSet):
    model = Day
    serializer_class = DaySerializer


class ProfilesViewset(
        VisibleModelAPIViewsetMixin,
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


# TODO remove this?
class UsersViewset(
        viewsets.generics.RetrieveUpdateAPIView,
        viewsets.generics.ListAPIView,
        viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    # TODO: another permission class to
    # check user.profile.private instead of user.private
    permission_classes = [IsAuthenticated]

    @action(methods=["GET"], detail=False)
    def active(self, request):
        """Returns currently active user"""
        user = request.user
        data = UserSerializer(user, context={"request": request}).data
        return Response(data)

    # TODO remove this?
    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return self.model.objects.all().filter(id=user.id)
