from django.db.models.signals import post_save
from django.dispatch import receiver
from blockbuster_clone.movies.models import Movie
from django.conf import settings
import requests
from rest_framework import status
from structlog import get_logger

logger = get_logger()


@receiver(post_save, sender=Movie)
def get_movie_info(sender, instance, created, **kwargs):
    if created:
        update_movie_info(instance)
    # elif "Error" in instance.info:
    #         update_movie_info(instance)


def update_movie_info(instance):
    # Convert this to a celery task
    # Make http requerst
    api_key = settings.OMDB_API_KEY
    if api_key == "NONE":
        pass
    else:
        current_movie_response = requests.get(
            "http://www.omdbapi.com/", params={"i": instance.imdb_id, "apiKey": api_key}
        )
        if current_movie_response.status_code != status.HTTP_200_OK:
            logger.error(
                "UpdatingMovie",
                data={
                    "status_code": current_movie_response.status_code,
                    "data": str(current_movie_response.text),
                },
            )
        else:
            json_response = current_movie_response.json()
            logger.debug("UpdatingMovie", data=json_response)
            item_type = json_response.get("Type")
            if item_type != "movie":
                instance.info = {"Error": "Not a movie!"}
            else:
                instance.info = json_response
            instance.save()