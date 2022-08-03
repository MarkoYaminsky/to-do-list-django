from django.urls import path

from .views import RegistrationAPIView

urlpatterns = [
    path('user/registration', RegistrationAPIView.as_view()),
]
