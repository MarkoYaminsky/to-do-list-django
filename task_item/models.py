from django.db import models


class TaskItem(models.Model):
    id = models.AutoField(primary_key=True)
    is_done = models.BooleanField(default=False)
    name = models.CharField(max_length=40)
    color = models.CharField(max_length=20)
    task_value = models.IntegerField()
    objects = models.Manager()
