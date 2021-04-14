from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from structlog import get_logger

from blockbuster_clone.store.models import Movement, Order
from blockbuster_clone.store.permissions import IsStaffOrSelf
from blockbuster_clone.store.serializers import MovementSerializer, OrderSerializer

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
        if self.request.user.is_staff_member:
            return Order.objects.all()
        else:
            return Order.objects.filter(created_by=self.request.user)

    @action(detail=True, methods=["post", "get"])
    def movements(self, request, pk=None):
        order = self.get_object()
        if self.request.method == "GET":
            movements_serializer = MovementSerializer(order.movements.all(), many=True)
            logger.debug(
                "OrderMovements",
                data={
                    "movements": order.movements.all(),
                    "serialized": movements_serializer.data,
                },
            )
            return Response(movements_serializer.data)
        serializer = MovementSerializer(data=request.data)
        if serializer.is_valid():
            logger.debug("AddMovement", data=serializer.validated_data)
            m = Movement.objects.create(
                **serializer.validated_data, order=order, user=self.request.user
            )
            return Response(MovementSerializer(m).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovementViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
    permission_classes = [IsStaffOrSelf]

    def get_queryset(self):
        if self.request.user.is_staff_member:
            return Movement.objects.all()
        else:
            return Movement.objects.filter(user=self.request.user)
