from django.db import models, IntegrityError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    def create_user(self, username, password):

        if not password:
            raise ValueError('User must have a password')

        if not username:
            raise ValueError('User must have a username')

        user = self.model(username=username)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password):

        if not password:
            raise ValueError('Superuser must have a password')

        if not username:
            raise ValueError('Superuser must have a username')

        user = self.model(username=username)
        user.set_password(password)
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)

    def get_or_create_token(self):
        try:
            token = Token.objects.create(user_id=self.id)
            return token.key
        except IntegrityError:
            token = Token.objects.get(user=self)
            return token.key

    token = property(get_or_create_token)
    USERNAME_FIELD = 'username'
    objects = UserManager()
