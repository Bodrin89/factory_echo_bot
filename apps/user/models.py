from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    last_name = None
    email = None
    bot_token = models.CharField(max_length=150, blank=True, null=True)
