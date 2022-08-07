from django.shortcuts import redirect, get_object_or_404
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

        return redirect('/taskitems')

    def list(self, request, *args, **kwargs):
        user = request.user
        tasks = user.taskitem_set.all()

        serializer = self.serializer_classes['list'](tasks, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskItemPatchDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    patch_serializer = TaskItemPatchSerializer
    queryset = TaskItem.objects.all()

    def delete(self, request, pk):
        user = request.user

        task = get_object_or_404(self.queryset.filter(user=user), id=pk)
        task.delete()

        return redirect('/taskitems')

    def patch(self, request, pk):
        data = request.data
        user = request.user
        serializer = self.patch_serializer()

        task = get_object_or_404(self.queryset.filter(user=user), id=pk)

        serializer.update(task, data)

        return redirect('/taskitems')
