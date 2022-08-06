from rest_framework import serializers

from to_do_list_django.apps.authentication.models import User
from to_do_list_django.apps.authentication.serializers import UserRegistrationLoginSerializer


class UserListSerializer(serializers.ModelSerializer):
    token = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'token')


class AdminUserRegistrationSerializer(UserRegistrationLoginSerializer):
    def create(self, validated_data):
        return User.objects.create_superuser(username=validated_data['username'], password=validated_data['password'])
