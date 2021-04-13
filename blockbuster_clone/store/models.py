from django.db import models
from decimal import Decimal

from blockbuster_clone.movies.models import Movie
from blockbuster_clone.users.models import User


# Create your models here.
class Movement(models.Model):
    class MovementType(models.IntegerChoices):
        SALE = 1
        RENT = 2
        RENT_RETURN = 3
        DEFECTIVE_RETURN = 4
        PURCHASE = 5
        ADJUSTMENT = 6

    movement_type = models.IntegerField(choices=MovementType.choices)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Sale(Movement):
    def __init__(self, *args, **kwargs):
        self._meta.get_field("movement_type").default = 1
        super(RentRequest, self).__init__(*args, **kwargs)


class RentRequest(Movement):

    penalty_fee = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal("0.00")
    )

    def __init__(self, *args, **kwargs):
        self._meta.get_field("movement_type").default = 2
        super(RentRequest, self).__init__(*args, **kwargs)


class RentReturn(Movement):
    def __init__(self, *args, **kwargs):
        self._meta.get_field("movement_type").default = 3
        super(RentReturn, self).__init__(*args, **kwargs)


class DefectiveReturn(Movement):
    reason = models.CharField(max_length=255, blank=False)

    def __init__(self, *args, **kwargs):
        self._meta.get_field("movement_type").default = 4
        super(DefectiveReturn, self).__init__(*args, **kwargs)


class Purchase(Movement):
    def __init__(self, *args, **kwargs):
        self._meta.get_field("movement_type").default = 5
        super(Purchase, self).__init__(*args, **kwargs)

class InventoryAdjustment(Movement):
    reason = models.CharField(max_length=255,blank=False)
    def __init__(self, *args, **kwargs):
        self._meta.get_field("movement_type").default = 5
        super(Purchase, self).__init__(*args, **kwargs)
