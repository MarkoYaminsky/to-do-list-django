from rest_framework import serializers
from .models import TaskItem


class TaskItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = ('color', 'name', 'task_value')


class TaskItemPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        field = ('is_done', 'name', 'color', 'task_value')

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
