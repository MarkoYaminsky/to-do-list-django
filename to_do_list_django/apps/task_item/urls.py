from django.urls import path

from to_do_list_django.apps.task_item import views

urlpatterns = [
    path('taskitems', views.TaskItemListCreateAPIView.as_view()),
    path('taskitems/delete/<pk>', views.TaskItemDeleteAPIView.as_view()),
    path('taskitems/patch/<pk>', views.TaskItemPatchAPIView.as_view())
]
