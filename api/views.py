import logging

from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from rest_framework import viewsets, views
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
logger.setLevel(logging.DEBUG)


class HabitsViewset(VisibleToUserObjectsMixin, viewsets.ModelViewSet):
    model = Habit
    serializer_class = HabitSerializer
    filterset_fields = ("active", "negative", "user", "private")
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


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request):
    """Returns current user."""
    user = request.user
    serializer = UserSerializer(user, context={'request': request})
    return Response(serializer.data, status=200)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_profile(request):
    """Returns current profile."""
    profile = request.user
    serializer = ProfileSerializer(profile, context={'request': request})
    return Response(serializer.data, status=200)


# class UsersViewset(
#         viewsets.generics.ListAPIView,
#         viewsets.generics.RetrieveAPIView,
#         viewsets.GenericViewSet):
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated & IsSameIdAsUser]
#
#     def get_queryset(self) -> QuerySet:
#         if self.request.user.is_staff:
#             queryset = User.objects.all()
#         else:
#             queryset = User.objects.all().filter(id=self.request.user.id)
#         return queryset
#
#     @action(methods=["GET"], detail=False)
#     def user_id(self, request):
#         pk = request.user.id
#         return Response({"pk": pk})
#
#
# class ProfilesViewset(
#         VisibleToUserObjectsMixin,
#         viewsets.generics.RetrieveUpdateAPIView,
#         viewsets.generics.ListAPIView,
#         viewsets.GenericViewSet):
#     model = Profile
#     serializer_class = ProfileSerializer
#
#     @action(methods=["GET"], detail=False)
#     def profile_id(self, request):
#         pk = request.user.profile.id
#         return Response({"pk": pk})
