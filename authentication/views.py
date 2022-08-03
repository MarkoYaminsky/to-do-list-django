from rest_framework import status
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

