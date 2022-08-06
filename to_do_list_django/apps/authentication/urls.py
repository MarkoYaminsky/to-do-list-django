from django.urls import path

from . import views

urlpatterns = [
    path('user/registration', views.UserRegistrationAPIView.as_view()),
    path('user/login', views.UserLoginAPIView.as_view())
]
