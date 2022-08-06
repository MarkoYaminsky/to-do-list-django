from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('to_do_list_django.apps.authentication.urls')),
    path('', include('to_do_list_django.apps.task_item.urls')),
    path('', include('to_do_list_django.apps.admin.urls'))
]
