from rest_framework.permissions import BasePermission


class SuperUserPermission(BasePermission):
    """
    超级管理员
    """

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return bool(request.user.is_superuser)
