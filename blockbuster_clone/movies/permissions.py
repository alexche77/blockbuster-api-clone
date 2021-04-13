from rest_framework import permissions
from structlog import get_logger

logger = get_logger()

class IsStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        logger.debug('Checking permissions')
        if request.method in permissions.SAFE_METHODS:
            return True        
        is_staff = request.user.is_staff_member
        logger.debug('Check::Movie::IsStaff', data=is_staff)
        return is_staff
