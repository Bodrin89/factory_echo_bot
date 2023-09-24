import os

import pytest

import logging
from django.urls import reverse

from apps.bot.services import SendMessageService

logger = logging.getLogger('main')


@pytest.mark.django_db
class TestBot:
    url = reverse('apps.bot:list-message')
    url_create = reverse('apps.bot:message')

    def test_get_list_message(self, get_auth_client, message, message_not_owner_factory):
        """Тест на получение списка сообщений авторизованным пользователем и получение только своих сообщений"""
        os.environ["TEST_ENV"] = "for_test"
        response = get_auth_client.get(self.url)
        not_owner_message = message_not_owner_factory()

        assert response.status_code == 200
        assert response.data[0]['text'] == message.text
        assert response.data[0]['text'] != not_owner_message.text

    def test_get_list_message_not_auth(self, client):
        """Тест на получение списка сообщений не авторизованным пользователем"""
        response = client.get(self.url)
        assert response.status_code == 403

    def test_create_message(self, get_auth_client, mocker, bot):
        """Тест на создание сообщения"""

        mocker.patch.object(SendMessageService, 'send_message')
        response_data = {'text': 'Test user text'}
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = response_data
        response = get_auth_client.post(self.url_create, data={'text': 'Test user text'})

        assert response.status_code == 201
        assert response.data['text'] == 'Test user text'

    def test_send_message_telegram(self, get_auth_client):
        """Тест на отправку сообщения без подтвержденного токена в телеграм"""

        response = get_auth_client.post(self.url_create, data={'text': 'Test user text'})
        except_message = 'У вас нет токена для отправки сообщений боту. Зайдите в личный кабинет и создайте токен, ' \
                         'затем авторизуйтесь через telegram-bot'
        assert response.data[0] == except_message
        assert response.status_code == 400
