from rest_framework import permissions
from structlog import get_logger

from blockbuster_clone.store.models import Order

logger = get_logger()


class IsStaffOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff_member


class IsStaffOrOrderPublic(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_staff = request.user.is_staff_member
        is_public_order_type = obj.order_type in [
            Order.OrderType.SALE,
            Order.OrderType.RENT,
            Order.OrderType.RENT_RETURN,
            Order.OrderType.DEFECTIVE_RETURN,
        ]
        logger.debug(
            "IsStaffOrOrderPublic", data={"is_public_order_type": is_public_order_type}
        )
        if is_staff:
            return True

        return is_public_order_type and obj.created_by == request.user
