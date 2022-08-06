from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from . import serializers
from ..authentication.models import User
from ...settings import SECRET_KEY


class AdminUserCreateAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.AdminUserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        if data['SECRET_KEY'] != SECRET_KEY:
            return Response({"detail": "Method POST forbidden"}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserListAPIView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = serializers.UserListSerializer
    queryset = User.objects.all()
