import logging

from django.conf import settings
from django.core.cache import cache
from rest_framework.request import Request

from apps.bot.models import Bot, Message
from apps.bot.utils import send_message

logger = logging.getLogger('main')


class SendMessageService:

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
        send_message(data)

        message = Message.objects.create(user=user, text=data_request.data.get('text'))
        message_list = Message.objects.select_related('user').all().filter(user_id=user.id)
        cache.set(message_cache_name, message_list, 60 * 60)

        return message
