from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatRoom(models.Model):
    room_name = models.CharField(max_length=100, verbose_name='채팅방명', unique=True)
    status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    class Meta:
        db_table='chat_room'


class ChatUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_user")
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="chat_user")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'chat_room'], name='user_chat_room_unique')
        ]
        db_table='chat_user'


class ChatMessage(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="chat_message")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="chat_message", null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    class Meta:
        db_table='chat_message'