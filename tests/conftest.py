from pytest_factoryboy import register

from tests.factories import BotFactory, MessageFactory, MessageNotOwnerFactory, UserFactory, UserNotOwnerFactory

pytest_plugins = 'tests.fixtures'

register(UserFactory)
register(MessageFactory)
register(UserNotOwnerFactory)
register(MessageNotOwnerFactory)
register(BotFactory)
