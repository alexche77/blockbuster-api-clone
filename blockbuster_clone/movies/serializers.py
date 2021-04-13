from rest_framework import serializers
from blockbuster_clone.movies.models import Movie
from rest_framework.validators import UniqueValidator


class MovieSerializer(serializers.Serializer):
    imdb_id = serializers.CharField(
        required=True,
        allow_blank=False,
        validators=[UniqueValidator(queryset=Movie.objects.all())],
    )
    info = serializers.JSONField(read_only=True)
    sales = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imdb_id = validated_data.get("imdb_id", instance.imdb_id)
        instance.save()
        return instance
