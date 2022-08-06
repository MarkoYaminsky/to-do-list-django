from django.urls import path
from . import views

urlpatterns = [
    path('adminpage/registration', views.AdminUserRegistrationAPIView.as_view()),
    path('adminpage/users', views.UserListAPIView.as_view()),
    path('adminpage/users/<pk>', views.UserRetrieveDeleteAPIView.as_view()),
]
