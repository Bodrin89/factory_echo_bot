import logging

import pytest
from django.urls import reverse

logger = logging.getLogger('main')


@pytest.mark.django_db
class TestUser:
    url_signup = reverse('apps.user:signup')
    url_token = reverse('apps.user:token-user')

    def test_signup(self, client, user):
        """Тест создания нового пользователя"""
        data = {'username': 'test_username',
                'first_name': 'test_username',
                'password': user.password,
                'password_repeat': user.password}

        response = client.post(self.url_signup, data=data)

        assert response.status_code == 200
        assert response.data == {'id': response.data['id'], 'username': data['username'],
                                 'first_name': data['first_name']}

    def test_create_token_auth(self, get_auth_client):
        """Тест на создание аутентифицированным пользователем токена"""

        response = get_auth_client.put(self.url_token, data={'bot_token': 'bot_token'})
        assert response.status_code == 200
        assert response.data['bot_token'] == 'bot_token'

    def test_create_token_not_auth(self, client):
        """Тест на создание аутентифицированным пользователем токена"""

        response = client.put(self.url_token, data={'bot_token': 'bot_token'})
        assert response.status_code == 403
