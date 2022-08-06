from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

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

        token = User.objects.get(username=user.username).token

        return Response({"username": user.username, "token": token}, status=status.HTTP_201_CREATED)


class UserListAPIView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = serializers.UserListSerializer

    def get_queryset(self):
        queryset = User.objects.all()

        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(username__contains=username)

        return queryset


class UserRetrieveDeleteAPIView(APIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()

    def get(self, request, pk):
        user = self.queryset.get(id=pk)
        serializer = serializers.UserListSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            user = self.queryset.get(id=pk)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data

        if user.is_staff is False:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        try:
            secret_key = data['SECRET_KEY']
        except KeyError:
            return Response({"detail": "Please provide SECRET_KEY in the request body to delete admin"})

        if secret_key == SECRET_KEY:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({"detail": "Invalid secret key"}, status=status.HTTP_403_FORBIDDEN)
