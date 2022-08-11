from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import UserRegistrationLoginSerializer


class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationLoginSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationLoginSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user = authenticate(username=data['username'], password=data['password'])

        if not user:
            try:
                User.objects.get(username=data['username'])
            except User.DoesNotExist:
                return Response("404 User not found", status=status.HTTP_404_NOT_FOUND)
            return Response("Invalid password", status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)