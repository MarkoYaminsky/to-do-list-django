from django.urls import path

from to_do_list_django.apps.task_item import views

urlpatterns = [
    path('taskitems', views.TaskItemListCreateAPIView.as_view()),
    path('taskitems/<pk>', views.TaskItemPatchDeleteAPIView.as_view())
]
