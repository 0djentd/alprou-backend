from rest_framework import generics, mixins
from rest_framework.permissions import IsAdminUser

from core.models import Profile

from . import serializers
from . mixins import IsObjectAuthorPermission


class ProfilesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


class ProfileDetailsAPIView(IsObjectAuthorPermission,
                            generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
