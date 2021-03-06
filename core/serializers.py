from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.HyperlinkedIdentityField("user-detail")

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["id", "url", "username",
                            "created", "modified", "user"]


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ["id", "url", "username", "profile", "habits", "days"]
        read_only_fields = ["id", "url", "username",
                            "profile", "habits", "days"]
