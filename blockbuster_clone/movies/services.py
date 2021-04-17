import requests
from django.conf import settings
from rest_framework import status
from structlog import get_logger

from blockbuster_clone.movies.exceptions import (
    InvalidCredentialError,
    MovieNotFound,
    RequestFailedError,
)

logger = get_logger()

API_URL = "http://www.omdbapi.com/"


class OmdbApi:
    def __init__(self):
        self.api_key = settings.OMDB_API_KEY
        if self.api_key is None:
            raise InvalidCredentialError

    def fetch_movie_by_imdb_id(self, imdb_id):
        current_movie_response = requests.get(
            API_URL, params={"i": imdb_id, "apiKey": self.api_key}
        )
        if current_movie_response.status_code != status.HTTP_200_OK:
            raise RequestFailedError(current_movie_response.json())
        else:
            json_response = current_movie_response.json()
            if "Error" in json_response:
                raise MovieNotFound(
                    message=json_response.get("Error", "Error from API"),
                    imdb_id=imdb_id,
                )
            item_type = json_response.get("Type")
            if item_type != "movie":
                raise MovieNotFound(imdb_id)
            return json_response
