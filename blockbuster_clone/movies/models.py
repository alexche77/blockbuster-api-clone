from django.db import models
from django_softdelete.models import SoftDeleteModel
from django.utils.functional import cached_property

# Create your models here.
class Movie(SoftDeleteModel):
    imdb_id = models.CharField(
        "IMDB ID used to fetch information",
        blank=False,
        null=False,
        max_length=25,
    )
    info = models.JSONField("Movie information", blank=True, null=True, default=None)
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

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["imdb_id"],
                condition=models.Q(is_deleted=False),
                name="unique_if_not_deleted",
            )
        ]

    def __str__(self):
        error = self.info.get('Error','Pending information')
        return f"{(self.info.get('Title') if (self.info and 'Error' not in self.info) else f'Movie # {self.imdb_id}: {error}')}"