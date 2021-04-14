from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from blockbuster_clone.movies.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
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
        instance.base_price_policy = validated_data.get(
            "base_price_policy", instance.base_price_policy
        )
        instance.profit_percentage = validated_data.get(
            "profit_percentage", instance.profit_percentage
        )
        instance.save()
        return instance


class MovieDetailSerializer(MovieSerializer):
    sales = serializers.IntegerField(default=0, read_only=True)
    stock = serializers.IntegerField(default=0, read_only=True)
    rents = serializers.IntegerField(default=0, read_only=True)
    rent_returns = serializers.IntegerField(default=0, read_only=True)
    defective_returns = serializers.IntegerField(default=0, read_only=True)
    purchases = serializers.ReadOnlyField()
    adjustments = serializers.IntegerField(default=0, read_only=True)
    final_price = serializers.DecimalField(
        default=Decimal("0.00"), max_digits=5, decimal_places=2, read_only=True
    )
    base_price = serializers.DecimalField(
        default=Decimal("0.00"), max_digits=5, decimal_places=2, read_only=True
    )
    highest_price = serializers.DecimalField(
        default=Decimal("0.00"), max_digits=5, decimal_places=2, read_only=True
    )
    average_price = serializers.DecimalField(
        default=Decimal("0.00"), max_digits=5, decimal_places=2, read_only=True
    )
    profit_percentage = serializers.FloatField(default=0)
    base_price_policy = serializers.IntegerField(
        default=1, validators=[MaxValueValidator(2), MinValueValidator(1)]
    )
