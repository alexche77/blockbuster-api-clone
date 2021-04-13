from django.db import models
from softdelete.models import SoftDeleteModel


# Create your models here.
class Movie(SoftDeleteModel):
    imdb_id = models.CharField(
        "IMDB ID used to fetch information", blank=False, null=False, unique=True
    )
    info = models.JSONField("Movie information", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    rental_price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    sale_price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    updated_at = models.DateTimeField(auto_now=True)
