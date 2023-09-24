import logging
from typing import Callable

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request

from apps.user.models import User
from apps.user.serializers import CreateUserSerializer


class UserServices:

    @staticmethod
    def signup_user(user_data: CreateUserSerializer) -> User:
        """Создание нового пользователя и сохранение его в БД с захэшированным паролем"""
        del user_data.validated_data['password_repeat']
        user_data.validated_data['password'] = make_password(user_data.validated_data['password'])
        user = User.objects.create(**user_data.validated_data)
        return user

    @staticmethod
    def login_user(user_data: Request, serializer_data: Callable) -> User:
        """Аутентификация пользователя"""
        if not (user := authenticate(
                username=user_data.data.get('username', None),
                password=user_data.data.get('password', None)
        )):
            raise AuthenticationFailed
        else:
            serializer = serializer_data(data={'username': user.username,
                                               'password': user.password})
            serializer.is_valid(raise_exception=True)
            return user

    @staticmethod
    def load_token(token: Request, serializer_data: Callable, user: User) -> User:
        """Создание токена для подтверждения в telegram боте"""
        serializer = serializer_data(data=token.data)
        serializer.is_valid(raise_exception=True)

        user.bot_token = serializer.validated_data['bot_token']
        user.save(update_fields=['bot_token'])

        return user
