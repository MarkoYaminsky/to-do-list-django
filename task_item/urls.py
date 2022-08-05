from django.urls import path

from task_item import views

urlpatterns = [
    path('taskitems', views.TaskItemListCreateAPIView.as_view()),
    path('taskitems/<pk>/delete', views.TaskItemDeleteAPIView.as_view()),
    path('taskitems/<pk>/patch', views.TaskItemPatchAPIView.as_view())
]
