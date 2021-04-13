from django.db import models
from django_softdelete.models import SoftDeleteModel
from django.utils.functional import cached_property

# Create your models here.
class Movie(SoftDeleteModel):
    imdb_id = models.CharField(
        "IMDB ID used to fetch information",
        blank=False,
        null=False,
        unique=True,
        max_length=25,
    )
    info = models.JSONField("Movie information", blank=False, null=False, default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @cached_property
    def sales(self):
        return self.sale.objects.count()

    @cached_property
    def rents(self):
        return self.rent.objects.count()

    @cached_property
    def rent_returns(self):
        return self.rent_return.objects.count()

    @cached_property
    def defective_returns(self):
        return self.defective_return.objects.count()

    @cached_property
    def purchases(self):
        return self.purchase.objects.count()

    @cached_property
    def adjustments(self):
        return self.adjustment.objects.count()