from rest_framework import serializers
from .models import User


class UserRegistrationLoginSerializer(serializers.ModelSerializer):
    token = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('username', 'password', 'token')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
