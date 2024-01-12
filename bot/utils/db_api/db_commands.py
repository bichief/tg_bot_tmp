from asgiref.sync import sync_to_async
from django.db import InterfaceError, connection

from admin_panel.telebot.models import Users


@sync_to_async
def create_user(telegram_id, name, username):
    try:
        Users.objects.get_or_create(
            telegram_id=telegram_id,
            name=name,
            username=username
        )
    except InterfaceError:
        connection.close()


@sync_to_async()
def get_user(telegram_id):
    try:
        return Users.objects.filter(telegram_id=telegram_id).first()
    except InterfaceError:
        connection.close()
