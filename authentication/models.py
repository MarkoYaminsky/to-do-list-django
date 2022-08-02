from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


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
    USERNAME_FIELD = 'username'
    objects = UserManager()
