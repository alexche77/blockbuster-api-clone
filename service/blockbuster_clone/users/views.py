from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .permissions import IsStaffOrSelf
from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsStaffOrSelf]
    queryset = User.objects.all()
    lookup_field = "username"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=True, methods=["POST"])
    def groups(self, request, username=None):
        user: User = self.get_object()
        if "group" not in request.data:
            raise ValidationError(detail={"group": "This field is required"})
        group_name = request.data["group"]
        if group_name == "User":
            user.groups.clear()
        else:
            group: Group = get_object_or_404(Group, name=group_name)
            user.groups.clear()
            group.user_set.add(user)
        return Response(status=status.HTTP_202_ACCEPTED)
