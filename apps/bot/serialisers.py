import logging

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.bot.models import Message

logger = logging.getLogger('main')


class CreateListMessageSerializer(ModelSerializer):
    """Сериализатор для создания сообщения и вывода всех сообщений пользователя"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = '__all__'
