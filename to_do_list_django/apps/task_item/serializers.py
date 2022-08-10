from rest_framework import serializers
from .models import TaskItem


class TaskItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = ('color', 'name', 'task_value', 'id')
        extra_kwargs = {'id': {'read_only': True}}


class TaskItemPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = ('is_done', 'name', 'color', 'task_value', 'id')

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance


class TaskItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = ('id', 'is_done', 'name', 'color', 'task_value')
