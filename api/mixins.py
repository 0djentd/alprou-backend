from rest_framework import permissions, authentication
from .permissions import IsObjectAuthorPermission


class ObjectPermissionsMixin():
    authentication_classes = [
        authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsObjectAuthorPermission]
