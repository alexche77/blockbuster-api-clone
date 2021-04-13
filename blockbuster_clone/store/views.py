from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from structlog import get_logger

from blockbuster_clone.store.models import Order
from blockbuster_clone.store.serializers import OrderSerializer

logger = get_logger()


class OrderViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        logger.debug(
            "OrderList", data={"is_staff_member": self.request.user.is_staff_member}
        )
        if self.request.user.is_staff_member:
            return Order.objects.all()
        else:
            return Order.objects.filter(created_by=self.request.user)
