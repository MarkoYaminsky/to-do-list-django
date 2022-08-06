from django.db import models
from to_do_list_django.apps.authentication.models import User


class TaskItem(models.Model):
    id = models.AutoField(primary_key=True)
    is_done = models.BooleanField(default=False)
    name = models.CharField(max_length=40)
    color = models.CharField(max_length=20)
    task_value = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    objects = models.Manager()
