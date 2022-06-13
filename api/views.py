from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from core.models import Profile

from . import serializers
from . mixins import IsObjectAuthorPermission


class ProfilesListAPIView(IsObjectAuthorPermission, generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsObjectAuthorPermission, IsAdminUser]
