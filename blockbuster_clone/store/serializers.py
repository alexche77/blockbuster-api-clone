from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
