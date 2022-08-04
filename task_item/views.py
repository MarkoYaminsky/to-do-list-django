from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import TaskItemCreateSerializer
from .serializers import TaskItemListSerializer


class TaskItemListCreationAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_classes = {'create': TaskItemCreateSerializer, 'list': TaskItemListSerializer}

    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user

        serializer = self.serializer_classes['create'](data=data)
        serializer.is_valid(raise_exception=True)
        item = serializer.save()

        user.taskitem_set.add(item)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        user = request.user
        tasks = user.taskitem_set.all()

        serializer = self.serializer_classes['list'](tasks, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
