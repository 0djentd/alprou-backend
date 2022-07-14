import logging

from rest_framework import permissions


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)


class _LogMixin:
    def log_check(self, result, req, view, obj=None):
        logger.debug("===============================================")
        logger.debug("checking permissions %s", self.__class__.__name__)
        if obj:
            method_name = "has_object_permission"
        else:
            method_name = "has_permission"
        logger.debug("method name: %s", method_name)
        logger.debug("req.method: %s", req.method)
        logger.debug("view: %s", view.__class__.__name__)
        if obj:
            logger.debug("obj: %s", obj)
        logger.debug("result: %s", result)


class IsObjectAuthorOrReadonlyIfVisible(
        _LogMixin, permissions.BasePermission):
    """
    Permission that allows other users to view object only if author
    specified that it should be visible.
    """

    def has_object_permission(self, req, view, obj):
        result = False
        if req.user == obj.user:
            result = True
        elif req.method in permissions.SAFE_METHODS:
            if not obj.private:
                result = True
        self.log_check(result, req, view, obj)
        return result
