from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.user.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации нового пользователя"""
    password = serializers.CharField(validators=[validate_password],
                                     write_only=True, style={'input_type': 'password'})
    password_repeat = serializers.CharField(write_only=True,
                                            style={'input_type': 'password'}, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'password', 'password_repeat')

    def validate(self, attrs: dict) -> dict:
        """Проверка введенного повторно пароля на валидность"""
        if not attrs.get('password_repeat', None):
            raise ValidationError('Required field')
        if attrs['password'] != attrs['password_repeat']:
            raise ValidationError('Password does not match')
        return attrs


class LoginSerializer(serializers.ModelSerializer):
    """Сериализатор для входа по username и password"""
    password = serializers.CharField(validators=[validate_password],
                                     write_only=True, style={'input_type': 'password'})
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'password')
        read_only_fields = ('id', 'first_name')


class TokenUserSerializer(serializers.ModelSerializer):
    """Сериализатор для создания токена"""

    class Meta:
        model = User
        fields = ('bot_token',)
