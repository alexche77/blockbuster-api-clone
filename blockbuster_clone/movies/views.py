from rest_framework.views import APIView
from blockbuster_clone.movies.models import Movie
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from blockbuster_clone.movies.serializers import MovieSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin

from rest_framework.viewsets import GenericViewSet

class MovieViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    lookup_field = 'imdb_id'

# class MovieList(APIView):
#     def get(self, request, format=None):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)