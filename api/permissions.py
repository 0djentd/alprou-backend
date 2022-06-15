import logging

from rest_framework import permissions


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class IsObjectAuthorPermission(permissions.DjangoObjectPermissions):
    def has_permission(self, req, view):
        logger.debug(req.user)
        logger.debug(req.user.is_staff)
        if req.user.is_staff:
            result = True
        else:
            result = False
        logger.debug(result)
        return result

    def has_object_permission(self, req, view, obj):
        logger.debug(req.user)
        logger.debug(obj.user)
        if req.user.id == obj.user.id:
            result = True
        else:
            result = False
        logger.debug(result)
        return result
