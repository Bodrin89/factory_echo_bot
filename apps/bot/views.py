import logging

from django.conf import settings
from django.core.cache import cache
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.bot.models import Bot, Message
from apps.bot.serialisers import CreateListMessageSerializer
from apps.bot.services import SendMessageService

logger = logging.getLogger('main')


class SendMessage(CreateAPIView):
    """Отправка сообщения"""
    serializer_class = CreateListMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        logger.debug(user)
        return Message.objects.select_related('user').filter(user_id=user.pk)

    def create(self, request, *args, **kwargs) -> Response:
        """Создание нового сообщения и запись данных в кэш"""
        try:
            message = SendMessageService.create_message(request)
            serializer = self.serializer_class(message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Bot.DoesNotExist:
            raise ValidationError(
                'У вас нет токена для отправки сообщений боту. Зайдите в личный кабинет и '
                'создайте токен, затем авторизуйтесь через telegram-bot')


class ListMessage(ListAPIView):
    """Получение списка всех сообщений пользователя"""
    serializer_class = CreateListMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if message_from_cache := cache.get(settings.MESSAGE_CACHE_NAME + str(user.id)):
            return message_from_cache
        return Message.objects.select_related('user').filter(user_id=user.pk)
