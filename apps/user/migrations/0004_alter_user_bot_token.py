# Generated by Django 4.2.4 on 2023-08-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_bot_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bot_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
