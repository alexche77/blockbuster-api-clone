from django.db.models.signals import post_save
from django.dispatch import receiver
from structlog import get_logger

from blockbuster_clone.movies.models import Movie
from blockbuster_clone.movies.services import OmdbApi

logger = get_logger()


@receiver(post_save, sender=Movie)
def get_movie_info(sender, instance, created, **kwargs):
    if created:
        if instance.info and "imdbID" in instance.info:
            api = OmdbApi()
            try:
                info_from_api = api.fetch_movie_by_imdb_id(instance.imdb_id)
            except Exception as e:
                logger.error("SignalSetMovieInfo", data=e)
            else:
                instance.info = info_from_api
