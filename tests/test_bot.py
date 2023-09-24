import pytest

import logging
from django.urls import reverse

from apps.bot.models import Bot, Message
from bot_task import settings

logger = logging.getLogger('main')


#
@pytest.mark.django_db
class TestBot:
    url = reverse('apps.bot:list-message')
    url_create = reverse('apps.bot:message')

    def test_get_list_message(self, get_auth_client, message, message_not_owner_factory):
        """Тест на получение списка сообщений авторизованным пользователем и получение только своих сообщений"""
        response = get_auth_client.get(self.url)
        not_owner_message = message_not_owner_factory()

        assert response.status_code == 200
        assert response.data[0]['text'] == message.text
        assert response.data[0]['text'] != not_owner_message.text

    def test_get_list_message_not_auth(self, client):
        """Тест на получение списка сообщений не авторизованным пользователем"""
        response = client.get(self.url)
        assert response.status_code == 403

    def test_create_message(self, get_auth_client):
        response = get_auth_client.post(self.url_create, data={'text': 'Test user text'})
        assert response.status_code == 203

#
# @pytest.mark.django_db
# class TestBot:
#
#
#     url = reverse('apps.bot:list-message')
#     url_create = reverse('apps.bot:message')
#
#     def test_get_list_message(self, get_auth_client, message_not_owner_factory, message_factory):
#         """Тест на получение списка сообщений авторизованным пользователем и получение только своих сообщений"""
#         response = get_auth_client.get(self.url)
#         current_user = response.wsgi_request.user
#         message = message_factory()
#         message.user = current_user
#         message_not_owner = message_not_owner_factory()
#         logger.debug(response.json())
#
#         assert response.data[0]['text'] != message_not_owner.text
#         assert response.data[0]['text'] == message.text
#         assert response.status_code == 200
