from rest_framework import serializers
from django.contrib.auth.models import User
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["id", "url", "username",
                            "created", "modified", "user"]


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "url", "profile", "habits", "days"]
        read_only_fields = ["id", "username", "url",
                            "profile", "habits", "days"]
