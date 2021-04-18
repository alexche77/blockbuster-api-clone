from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied, ValidationError
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
from blockbuster_clone.store.permissions import IsStaffOrOrderPublic, IsStaffOrSelf
from blockbuster_clone.store.serializers import MovementSerializer, OrderSerializer

logger = get_logger()


class OrderViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    GenericViewSet,
    DestroyModelMixin,
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsStaffOrOrderPublic]

    def create(self, request, *args, **kwargs):
        is_staff = request.user.is_staff_member
        is_public_order_type = "order_type" in request.data and request.data[
            "order_type"
        ] in [
            Order.OrderType.SALE,
            Order.OrderType.RENT,
            Order.OrderType.RENT_RETURN,
            Order.OrderType.DEFECTIVE_RETURN,
        ]
        logger.debug(
            "OrderViewSet::create",
            data={"is_public_order_type": is_public_order_type, "is_staff": is_staff},
        )
        if is_staff and "order_type" not in request.data:
            request.data["order_type"] = Order.OrderType.PURCHASE
        if not is_public_order_type and not is_staff:
            raise PermissionDenied("Operation not permitted")
        return super(OrderViewSet, self).create(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_staff_member:
            return Order.objects.all()
        else:
            return Order.objects.filter(created_by=self.request.user)

    @action(detail=True, methods=["post", "get"])
    def movements(self, request, pk=None):
        order: Order = self.get_object()
        if self.request.method == "GET":
            movements_serializer = MovementSerializer(order.movements.all(), many=True)
            logger.debug(
                "OrderMovements",
                data={
                    "movements": order.movements.prefetch_related("movie").all(),
                    "serialized": movements_serializer.data,
                },
            )
            return Response(movements_serializer.data)
        if order.order_state != Order.OrderState.DRAFT:
            raise PermissionDenied("Order is accepted, movements cannot be added")
        serializer = MovementSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            logger.debug("MovementSerializer", data=data)
            movie = data["movie_id"]
            if order.movements.filter(movie=movie).exists():
                raise ValidationError(
                    detail={"detail": "Movie is already added to order"}
                )
            if order.order_type == Order.OrderType.SALE:
                data["price"] = movie.final_price
            elif order.order_type == Order.OrderType.RENT:
                data["price"] = movie.rent_price
            m = Movement.objects.create(**data, order=order)
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
    pagination_class = None
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
    permission_classes = [IsStaffOrSelf]

    def get_queryset(self):
        if self.request.user.is_staff_member:
            return Movement.objects.all()
        else:
            return Movement.objects.filter(order__created_by=self.request.user)
