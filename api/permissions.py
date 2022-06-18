import logging

from rest_framework import permissions


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)


class _log_mixin():
    def log_check(self, result, req, view, obj=None):
        logger.debug("===============================================")
        logger.debug(f"checking permissions '{self.__class__.__name__}'")
        if obj:
            method_name = "has_object_permission"
        else:
            method_name = "has_permission"
        logger.debug(f"method name: {method_name}")
        logger.debug(f"req.method: {req.method}")
        logger.debug(f"view: {view.__class__.__name__}")
        if obj:
            logger.debug(f"obj: {obj}")
        logger.debug(f"result: {result}")


class IsObjectAuthor(_log_mixin, permissions.BasePermission):
    """Object author can modify it."""

    def has_object_permission(self, req, view, obj):
        result = False
        if req.user.id == obj.user.id:
            result = True
        self.log_check(result, req, view, obj)
        return result


class IsObjectPublic(_log_mixin, permissions.BasePermission):
    """Other users can see object, but cant modify it."""

    def has_object_permission(self, req, view, obj):
        result = False
        if obj.user.id != req.user.id and obj.public:
            if req.method in permissions.SAFE_METHODS:
                result = True
        self.log_check(result, req, view, obj)
        return result


class IsSameIdAsUser(_log_mixin, permissions.BasePermission):
    def has_object_permission(self, req, view, obj):
        result = False
        if obj.id == req.user.id:
            result = True
        self.log_check(result, req, view, obj)
        return result
