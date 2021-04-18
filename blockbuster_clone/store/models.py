from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.functional import cached_property

from blockbuster_clone.users.models import User


class Order(models.Model):
    class OrderState(models.IntegerChoices):
        DRAFT = 0, "DRAFT"
        PENDING_REVIEW = 1, "PENDING REVIEW"
        REJECTED = 2, "REJECTED"
        ACCEPTED = 3, "ACCEPTED"

    class OrderType(models.IntegerChoices):
        SALE = 1, "SALE"
        RENT = 2, "RENT"
        RENT_RETURN = 3, "RENT_RETURN"
        DEFECTIVE_RETURN = 4, "DEFECTIVE RETURN"
        PURCHASE = 5, "PURCHASE"
        ADJUSTMENT_ADD = 6, "ADJUSTMENT ADD"
        ADJUSTMENT_REMOVE = 7, "ADJUSTMENT REMOVE"

    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_type = models.IntegerField(
        choices=OrderType.choices, default=OrderType.SALE, blank=False
    )
    order_state = models.IntegerField(
        choices=OrderState.choices, default=OrderState.DRAFT, blank=False
    )

    @cached_property
    def type_label(self):
        return self.OrderType(self.order_type).label

    @cached_property
    def state_label(self):
        return self.OrderState(self.order_state).label

    def __str__(self):
        return f"# {self.pk} - {self.type_label} - {self.state_label}"

    class Meta:
        ordering = ["-updated_at"]


class Movement(models.Model):
    movie = models.ForeignKey("movies.Movie", on_delete=models.PROTECT)
    order = models.ForeignKey(Order, related_name="movements", on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    comments = models.CharField(max_length=255, default=None, blank=True, null=True)
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    unit_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie} - {self.order}"

    class Meta:
        unique_together = ["movie", "order"]
        ordering = ["-created_at"]
