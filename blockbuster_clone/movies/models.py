from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Avg, Sum
from django.utils.functional import cached_property
from django_softdelete.models import SoftDeleteModel
from structlog import get_logger

from blockbuster_clone.store.models import Movement

logger = get_logger()


class Movie(SoftDeleteModel):
    class MoviePricePolicy(models.IntegerChoices):
        AVERAGE = 1, "AVERAGE"
        HIGHEST = 2, "HIGHEST"

    imdb_id = models.CharField(
        "IMDB ID used to fetch information",
        blank=False,
        null=False,
        max_length=25,
    )
    info = models.JSONField("Movie information", blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rent_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal("0.00"),
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    profit_percentage = models.FloatField(
        "Profit percentage for this movie",
        help_text="Will be applied to base price, based on pase price policy",
        default=0,
        validators=[MinValueValidator(0)],
    )
    base_price_policy = models.IntegerField(choices=MoviePricePolicy.choices, default=1)

    def get_price_policy(self):
        return self.MoviePricePolicy(self.base_price_policy).label

    @cached_property
    def stock(self):
        return (
            self.purchases
            - self.sales
            - self.defective_returns
            - self.rents
            + self.rent_returns
            + self.adjustments_add
            - self.adjustments_remove
        )

    @cached_property
    def base_price(self):
        logger.debug(
            "BasePrice",
            data={"policy": self.get_price_policy(), "highest": self.highest_price},
        )
        return (
            self.highest_price
            if self.base_price_policy == Movie.MoviePricePolicy.HIGHEST
            else self.average_price
        )

    @cached_property
    def final_price(self):
        price = self.base_price + (
            (Decimal.from_float(self.profit_percentage) / Decimal(100))
            * self.base_price
        )
        return price if price else 0

    @cached_property
    def highest_price(self):
        price = self.movement_set.order_by("-unit_price").first().unit_price
        return price if price else 0

    @cached_property
    def average_price(self):
        price = self.movement_set.aggregate(Avg("unit_price")).get(
            "unit_price__avg", Decimal("0.00")
        )

        return price if price else 0

    @cached_property
    def sales(self):
        count = (
            self.movement_set.filter(movement_type=Movement.MovementType.SALE)
            .aggregate(Sum("quantity"))
            .get("quantity__sum", 0)
        )
        return count if count else 0

    @cached_property
    def rents(self):
        count = (
            self.movement_set.filter(movement_type=Movement.MovementType.RENT)
            .aggregate(Sum("quantity"))
            .get("quantity__sum", 0)
        )
        return count if count else 0

    @cached_property
    def rent_returns(self):
        count = (
            self.movement_set.filter(movement_type=Movement.MovementType.RENT_RETURN)
            .aggregate(Sum("quantity"))
            .get("quantity__sum", 0)
        )
        return count if count else 0

    @cached_property
    def defective_returns(self):
        count = (
            self.movement_set.filter(
                movement_type=Movement.MovementType.DEFECTIVE_RETURN
            )
            .aggregate(Sum("quantity"))
            .get("quantity__sum", 0)
        )
        return count if count else 0

    @cached_property
    def purchases(self):
        count = (
            self.movement_set.filter(movement_type=Movement.MovementType.PURCHASE)
            .aggregate(Sum("quantity"))
            .get("quantity__sum", 0)
        )
        return count if count else 0

    @cached_property
    def adjustments_add(self):
        count = (
            self.movement_set.filter(movement_type=Movement.MovementType.ADJUSTMENT_ADD)
            .aggregate(Sum("quantity"))
            .get("quantity__sum", 0)
        )
        return count if count else 0

    @cached_property
    def adjustments_remove(self):
        count = (
            self.movement_set.filter(
                movement_type=Movement.MovementType.ADJUSTMENT_REMOVE
            )
            .aggregate(Sum("quantity"))
            .get("quantity__sum", 0)
        )
        return count if count else 0

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["imdb_id"],
                condition=models.Q(is_deleted=False),
                name="unique_if_not_deleted",
            )
        ]

    def __str__(self):
        error = self.info.get("Error", "Pending information")
        has_error = self.info and "Error" not in self.info
        return f"{(self.info.get('Title') if has_error else f'Movie # {self.imdb_id}: {error}')}"
