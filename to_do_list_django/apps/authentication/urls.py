from django.urls import path

from .views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    path('user/registration', RegistrationAPIView.as_view()),
    path('user/login', LoginAPIView.as_view())
]
