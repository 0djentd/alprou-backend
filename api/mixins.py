import logging

from django.db.models import Model
from django.db.models.base import ModelBase
from django.db.models.query import QuerySet
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.request import Request

from .permissions import IsObjectAuthorOrReadonlyIfVisible


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class VisibleModelAPIViewsetMixin:
    model: ModelBase
    request: Request

    permission_classes = [IsAuthenticated & IsObjectAuthorOrReadonlyIfVisible]

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        if self.request.method in SAFE_METHODS:
            return self.model.objects.all().filter(private=False) | self.model.objects.all().filter(user=user)
        return self.model.objects.all().filter(user=user)
