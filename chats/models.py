from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
# Create your models here.

User = get_user_model()
class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats')


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField
    timestamp = models.DateTimeField(auto_now_add=True)





