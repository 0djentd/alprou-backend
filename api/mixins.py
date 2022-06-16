import logging

from django.db.models import Model
from django.db.models.query import QuerySet
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated

from . permissions import IsObjectPublic, IsObjectAuthor


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class VisibleObjectsMixin():
    model: Model
    authentication_classes = [
        authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [IsAuthenticated & (IsObjectPublic | IsObjectAuthor)]

    def get_queryset(self) -> QuerySet:
        q_1 = self.model.objects.all().filter(public=True)
        q_2 = self.model.objects.all().filter(user=self.request.user)
        return q_1 | q_2
