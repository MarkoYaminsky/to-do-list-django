from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import UserRegistrationSerializer


class RegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "username": data['username'],
            "token": User.objects.get(username=data['username']).token().key
        }, status=status.HTTP_201_CREATED)


class LoginAPIView(CreateAPIView):
    def create(self, request, *args, **kwargs):
        data = request.data
        user = authenticate(username=data['username'], password=data['password'])

        if not user:
            return Response("404 USER NOT FOUND", status=status.HTTP_404_NOT_FOUND)

        token = Token.objects.get(user=user).key
        return Response(token, status=status.HTTP_200_OK)
