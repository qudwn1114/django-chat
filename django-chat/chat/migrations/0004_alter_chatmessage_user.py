# Generated by Django 4.2.11 on 2024-04-20 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0003_chatuser_user_chat_room_unique"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatmessage",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="chat_message",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
