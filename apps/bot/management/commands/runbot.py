from django.core.management import BaseCommand

from apps.bot.tg.client import bot


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Запуск telegram-бота"""
        bot.infinity_polling()
