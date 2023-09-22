import telebot
from telebot.types import Message

from apps.bot.models import Bot
from apps.user.models import User
from bot_task.settings import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def input_token(message: Message) -> None:
    """Обработчик команды '/start' с ожиданием ответа"""
    bot.send_message(message.chat.id, 'Введите токен!')
    bot.register_next_step_handler(message, save_token)


def save_token(message: Message) -> None:
    """Функция принимает токен от пользователя и проверяет есть ли такой токен"""
    token = message.text
    try:
        user = User.objects.get(bot_token=token)
        Bot.objects.get_or_create(chat_id=message.chat.id, user=user)
        bot.send_message(message.chat.id, 'Токен подтвержден!')
    except User.DoesNotExist:
        bot.send_message(message.chat.id, 'Такого пользователя не существует')


@bot.message_handler()
def some_cmd(message: Message) -> None:
    """Обработчик остальных команд"""
    bot.send_message(message.chat.id, 'Не известная команда')
