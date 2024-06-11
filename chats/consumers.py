import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat_group_name = f"chat_{self.chat_id}"

        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': "user_online",
                'user': self.scope['user'].username
            }
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'user_offline',
                'user': self.scope["user"].username
            }
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        typing = data.get('typing', False)

        if typing:
            await self.channel_layer.group_send(
                self.chat_group_name,
                {
                    'type': 'user_typing',
                    'user': self.scope["user"].username
                }
            )
        else:
            await self.channel_layer.group_send(
                self.chat_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'user': self.scope["user"].username
                }
            )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        await  self.send(text_data=json.dumps({
            'message': message,
            'user': user
        }))

    async def user_online(self, event):
        user = event['user']

        await self.send(text_data=json.dumps({
            'type': 'user_online',
            'user': user
        }))

    async def user_offline(self, event):
        user = event['user']

        await self.send(text_data=json.dumps({
            'type': 'user_offline',
            'user': user
        }))

    async def user_typing(self, event):
        user = event['user']

        await self.send(text_data=json.dumps({
            'type': 'user_typing',
            'user': user
        }))



















