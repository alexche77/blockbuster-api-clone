from django.db import models

from blockbuster_clone.movies.models import Movie


# Create your models here.
class Movements(models.Model):
    class MovementType(models.IntegerChoices):
        IN = 1
        OUT = 2

    movement_type = models.IntegerField(choices=MovementType.choices)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
