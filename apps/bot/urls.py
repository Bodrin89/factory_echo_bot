from django.urls import path

from apps.bot.views import ListMessage, SendMessage

urlpatterns = [
    path('message', SendMessage.as_view(), name='message'),
    path('message/list', ListMessage.as_view(), name='list-message'),
]
