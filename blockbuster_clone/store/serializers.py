from django.contrib.auth import get_user_model
from rest_framework import serializers
from structlog import get_logger

from blockbuster_clone.movies.serializers import MovieSerializer
from blockbuster_clone.store.models import Movement, Order

logger = get_logger()

User = get_user_model()


class OrderSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    type_label = serializers.ReadOnlyField()
    state_label = serializers.ReadOnlyField()

    class Meta:
        fields = "__all__"
        model = Order


class MovementSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )

    movie_id = serializers.IntegerField(required=True)

    movie = MovieSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    def validate_user(self, value):
        return self.context["request"].user

    class Meta:
        fields = "__all__"
        model = Movement
