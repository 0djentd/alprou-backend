import logging

from django.db.models import Model
from django.db.models.query import QuerySet
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated

from .permissions import IsObjectAuthor


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class VisibleToUserObjectsMixin:
    model: Model
    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication,
    ]
    permission_classes = [IsAuthenticated & IsObjectAuthor]

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return self.model.objects.all().filter(user=user)
