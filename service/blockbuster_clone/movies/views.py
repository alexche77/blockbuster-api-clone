from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from structlog import get_logger

from blockbuster_clone.movies.models import Movie
from blockbuster_clone.movies.permissions import IsStaff
from blockbuster_clone.movies.serializers import MovieDetailSerializer, MovieSerializer

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
