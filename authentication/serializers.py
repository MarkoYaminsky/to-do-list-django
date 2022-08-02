from rest_framework import serializers
from models import User


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'token')
