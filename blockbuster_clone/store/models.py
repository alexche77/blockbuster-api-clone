from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from blockbuster_clone.users.models import User


# Create your models here.
class Movement(models.Model):
    class MovementType(models.IntegerChoices):
        SALE = 1, "SALE"
        RENT = 2, "RENT"
        RENT_RETURN = 3, "RENT_RETURN"
        DEFECTIVE_RETURN = 4, "DEFECTIVE_RETURN"
        PURCHASE = 5, "PURCHASE"
        ADJUSTMENT_ADD = 6, "ADJUSTMENT_ADD"
        ADJUSTMENT_REMOVE = 7, "ADJUSTMENT_REMOVE"

    movement_type = models.IntegerField(choices=MovementType.choices)
    movie = models.ForeignKey("movies.Movie", on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    comments = models.CharField(max_length=255, default=None, blank=True)
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        default=Decimal("0.00"),
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    unit_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        default=Decimal("0.00"),
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def get_type(self):
        return self.MovementType(self.movement_type).label

    def __str__(self):
        return f"{self.movie} - {self.get_type()}"


class Order(models.Model):
    class OrderState(models.IntegerChoices):
        DRAFT = 0, "DRAFT"
        PENDING_REVIEW = 1, "PENDING_REVIEW"
        REJECTED = 2, "REJECTED"
        ACCEPTED = 3, "ACCEPTED"
        DEFECTIVE_RETURN = 4, "DEFECTIVE_RETURN"
        PURCHASE = 5, "PURCHASE"
        ADJUSTMENT = 6, "ADJUSTMENT"

    class OrderType(models.IntegerChoices):
        SALE = 1, "SALE"
        RENT = 2, "RENT"
        RENT_RETURN = 3, "RENT_RETURN"
        DEFECTIVE_RETURN = 4, "DEFECTIVE_RETURN"
        PURCHASE = 5, "PURCHASE"
        ADJUSTMENT_ADD = 6, "ADJUSTMENT_ADD"
        ADJUSTMENT_REMOVE = 7, "ADJUSTMENT_REMOVE"

    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    movie_purchase = models.ManyToManyField(Movement)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_type = models.IntegerField(
        choices=OrderType.choices, default=OrderType.SALE, blank=False
    )
    order_state = models.IntegerField(
        choices=OrderState.choices, default=OrderState.DRAFT, blank=False
    )

    def get_type(self):
        return self.OrderType(self.order_type).label

    def get_state(self):
        return self.OrderState(self.order_state).label
