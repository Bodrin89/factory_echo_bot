from pytest_factoryboy import register

from tests.factories import UserFactory, MessageFactory, UserNotOwnerFactory, MessageNotOwnerFactory

pytest_plugins = 'tests.fixtures'

register(UserFactory)
register(MessageFactory)
register(UserNotOwnerFactory)
register(MessageNotOwnerFactory)
