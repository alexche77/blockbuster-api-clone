from django.db import models
from django_softdelete.models import SoftDeleteModel


# Create your models here.
class Movie(SoftDeleteModel):
    imdb_id = models.CharField(
        "IMDB ID used to fetch information", blank=False, null=False, unique=True, max_length=25
    )
    info = models.JSONField("Movie information", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)
