from django.urls import path

from .views import TaskItemListCreationAPIView

urlpatterns = [
    path('taskitems', TaskItemListCreationAPIView.as_view())
]
