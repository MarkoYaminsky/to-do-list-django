from rest_framework import serializers

from to_do_list_django.apps.authentication.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff')


class AdminUserRegistrationSerializer(serializers.ModelSerializer):
    SECRET_KEY = serializers.CharField()

    class Meta:
        model = User
        fields = ('SECRET_KEY', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_superuser(username=validated_data['username'], password=validated_data['password'])
