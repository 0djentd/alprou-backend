import logging

from django.db.models import Model
from django.db.models.query import QuerySet
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated

from .permissions import IsObjectPublic, IsObjectAuthor


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class VisibleObjectsMixin:
    model: Model
    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication,
    ]
    permission_classes = [IsAuthenticated & (IsObjectPublic | IsObjectAuthor)]

    def get_queryset(self) -> QuerySet:
        logging.debug("Getting queryset for " + str(self.model))
        logging.debug("user:" + str(self.request.user))
        q_1 = self.model.objects.all().filter(private=False)
        q_2 = self.model.objects.all().filter(user=self.request.user)
        result = q_1 | q_2
        logging.debug(q_1)
        logging.debug(q_2)
        logging.debug(result)
        return result
