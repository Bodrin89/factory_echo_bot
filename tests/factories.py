import uuid

import factory.django

from apps.bot.models import Message
from apps.user.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    password = factory.Faker('password')
    bot_token = factory.Faker('password')


#
class UserNotOwnerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    password = factory.Faker('password')
    bot_token = factory.Faker('password')


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message

    created = factory.Faker('date')
    text = factory.Faker('text')
    user = factory.SubFactory(UserFactory)


#
class MessageNotOwnerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message

    created = factory.Faker('date')
    text = factory.Faker('text')
    user = factory.SubFactory(UserNotOwnerFactory)
