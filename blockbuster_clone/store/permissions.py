from rest_framework import permissions
from structlog import get_logger

logger = get_logger()


class IsStaffOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff_member
