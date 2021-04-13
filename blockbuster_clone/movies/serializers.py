from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from blockbuster_clone.movies.models import Movie


class MovieSerializer(serializers.Serializer):
    imdb_id = serializers.CharField(
        required=True,
        allow_blank=False,
        validators=[UniqueValidator(queryset=Movie.objects.all())],
    )
    info = serializers.JSONField(read_only=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imdb_id = validated_data.get("imdb_id", instance.imdb_id)
        instance.save()
        return instance


class MovieDetailSerializer(MovieSerializer):
    sales = serializers.IntegerField(default=0, read_only=True)
    rents = serializers.IntegerField(default=0, read_only=True)
    rent_returns = serializers.IntegerField(default=0, read_only=True)
    defective_returns = serializers.IntegerField(default=0, read_only=True)
    purchases = serializers.IntegerField(default=0, read_only=True)
    adjustments = serializers.IntegerField(default=0, read_only=True)
