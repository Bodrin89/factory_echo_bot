from django.db import models

from apps.user.models import User


class Message(models.Model):
    """Модель сообщений пользователя"""
    created = models.DateField(auto_now_add=True)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Bot(models.Model):
    """Модель бота telegram"""
    chat_id = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
