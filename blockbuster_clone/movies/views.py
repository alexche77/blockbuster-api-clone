from rest_framework.exceptions import APIException
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from structlog import get_logger

from blockbuster_clone.movies.exceptions import (
    InvalidCredentialError,
    MovieNotFound,
    RequestFailedError,
)
from blockbuster_clone.movies.models import Movie
from blockbuster_clone.movies.permissions import IsStaff
from blockbuster_clone.movies.serializers import MovieDetailSerializer, MovieSerializer
from blockbuster_clone.movies.services import OmdbApi

logger = get_logger()


class MovieViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    GenericViewSet,
):
    queryset = Movie.objects.all()
    permission_classes = [IsStaff]
    lookup_field = "imdb_id"

    def get_serializer_class(self):
        if self.request.user.is_authenticated and self.request.user.is_staff_member:
            return MovieDetailSerializer
        else:
            return MovieSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_staff_member:
            return Movie.objects.all()
        else:
            return Movie.objects.filter(info__Error__isnull=True)

    def retrieve(self, request, imdb_id=None):
        try:
            m = Movie.objects.get(imdb_id=imdb_id)
        except Movie.DoesNotExist:
            try:
                service = OmdbApi()
                movie_info = service.fetch_movie_by_imdb_id(imdb_id)
            except (RequestFailedError, MovieNotFound, InvalidCredentialError) as ex:
                logger.debug("RetrieveMovie ", data=str(ex))
                raise APIException(ex)
            else:
                m = Movie.objects.create(imdb_id=imdb_id, info=movie_info)
        serializer = self.get_serializer_class()
        return Response(data=serializer(m).data)
