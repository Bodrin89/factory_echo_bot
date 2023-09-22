import logging

import requests

from bot_task.settings import SEND_MESSAGE_URL

logger = logging.getLogger('main')


def send_message(data: dict) -> None:
    """Функция отправляющая сообщение telegram боту"""
    response = requests.post(SEND_MESSAGE_URL, data=data)

    if response.status_code == 200:
        logger.debug('Сообщение успешно отправлено!')
    else:
        logger.debug('Произошла ошибка при отправке сообщения.', response.text)
