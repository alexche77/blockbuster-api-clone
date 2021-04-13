from rest_framework.views import APIView
from blockbuster_clone.movies.models import Movie
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from blockbuster_clone.movies.serializers import MovieSerializer
from blockbuster_clone.movies.permissions import IsStaff
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)

from rest_framework.viewsets import GenericViewSet

from structlog import  get_logger

logger = get_logger()

class MovieViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    GenericViewSet,
):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()    
    lookup_field = "imdb_id"

    def get_queryset(self):
        logger.debug('MoviesList', data={'is_staff_member':self.request.user.is_staff_member})
        if self.request.user.is_staff_member:
            return Movie.objects.all()
        else:
            return Movie.objects.filter(info__Error__isnull=True)
    

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not self.request.user.is_staff_member and (instance.info is None or 'Error' in instance.info):
            raise Http404()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)