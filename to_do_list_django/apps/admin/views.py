from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from . import serializers
from to_do_list_django.settings import SECRET_KEY
from ..authentication.models import User


class AdminUserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.AdminUserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        if data['SECRET_KEY'] != SECRET_KEY:
            return Response({"detail": "Method POST forbidden"}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = User.objects.get(username=user.username).token()

        return Response({"username": user.username, "token": token.key}, status=status.HTTP_201_CREATED)


class UserListAPIView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = serializers.UserListSerializer
    queryset = User.objects.all()

