from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TaskItemCreateSerializer
from .serializers import TaskItemListSerializer
from .serializers import TaskItemPatchSerializer

from .models import TaskItem


class TaskItemListCreateAPIView(ListCreateAPIView):
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


class TaskItemDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = TaskItem.objects.all()

    def delete(self, request, pk):
        user = request.user

        try:
            task = self.queryset.filter(user=user).get(id=pk)
        except TaskItem.DoesNotExist:
            return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        task.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskItemPatchAPIView(APIView):
    serializer = TaskItemPatchSerializer
    permission_classes = (IsAuthenticated,)
    queryset = TaskItem.objects.all()

    def patch(self, request, pk):
        data = request.data
        user = request.user
        serializer = self.serializer()

        try:
            task = self.queryset.filter(user=user).get(id=pk)
        except TaskItem.DoesNotExist:
            return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer.update(task, data)

        return Response(status=status.HTTP_204_NO_CONTENT)