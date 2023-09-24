import logging

import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework.request import Request

from apps.bot.models import Bot, Message
from bot_task.settings import SEND_MESSAGE_URL

logger = logging.getLogger('main')


class SendMessageService:

    @staticmethod
    def send_message(data: dict) -> None:
        """Функция отправляющая сообщение telegram боту"""
        response = requests.post(SEND_MESSAGE_URL, data=data)

        if response.status_code == 200:
            logger.debug('Сообщение успешно отправлено!')
        else:
            logger.debug('Произошла ошибка при отправке сообщения.', response.text)

    @staticmethod
    def create_message(data_request: Request) -> Message:
        """Функция создание нового сообщения и запись данных в кэш"""
        user = data_request.user

        message_cache_name = settings.MESSAGE_CACHE_NAME + str(user.id)
        obj = Bot.objects.select_related('user').get(user_id=user.pk)
        data = {
            'chat_id': obj.chat_id,
            'text': f"{user.username},я получил от тебя сообщение\n{data_request.data['text']}"
        }
        SendMessageService.send_message(data)

        message = Message.objects.create(user=user, text=data_request.data.get('text'))
        message_list = Message.objects.select_related('user').all().filter(user_id=user.id)
        cache.set(message_cache_name, message_list, 60 * 60)

        return message
