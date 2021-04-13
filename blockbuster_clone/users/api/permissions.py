from rest_framework import permissions


class IsStaffOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.pk == request.user.pk:
            return True
        return request.user.is_staff_member and not obj.is_admin_member
