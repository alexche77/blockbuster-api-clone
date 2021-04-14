from django.contrib.auth import get_user_model
from rest_framework import serializers

from blockbuster_clone.store.models import Movement, Order

User = get_user_model()


class MovementSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )

    def validate_user(self, value):
        return self.context["request"].user

    class Meta:
        exclude = ["order"]
        model = Movement


class OrderSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        fields = "__all__"
        model = Order
