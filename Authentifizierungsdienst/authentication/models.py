import random
import uuid

from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class UserManager(BaseUserManager):

    def create_user_object(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')
        user = self.model(username=username, email=self.normalize_email(email),
                          created_at=timezone.now(), updated_at=timezone.now())
        user.set_password(password)
        return user

    def create_user(self, username, email, password=None):
        user = self.create_user_object(username, email, password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


AUTH_PROVIDERS = {'google': 'google', 'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True, unique=True, blank=True, editable=False)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        while not self.id:
            newid = int.from_bytes(random.randbytes(5))
            if not User.objects.filter(pk=newid).exists():
                self.id = newid
        super(User, self).save()

    def tokens(self):
        extra_data = {
            "user_name": self.username,
        }

        refresh = RefreshToken.for_user(self)
        refresh.payload.update(extra_data)

        access = AccessToken.for_user(self)
        access.payload.update(extra_data)
        return {
            'refresh': str(refresh),
            'access': str(access)
        }
