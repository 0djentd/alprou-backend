import logging

from rest_framework import permissions, authentication
from .permissions import IsObjectAuthorPermission


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ObjectPermissionsMixin():
    authentication_classes = [
        authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsObjectAuthorPermission]
