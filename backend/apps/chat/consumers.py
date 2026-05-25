import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import ChatRoom, Message

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"chat_{self.room_id}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)

        message = data.get("message")
        sender_id = data.get("sender")

        # SAVE MESSAGE TO DB (IMPORTANT FIX)
        msg = await self.save_message(self.room_id, sender_id, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": msg.text,
                "sender": sender_id,
                "message_id": msg.id,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "sender": event["sender"],
            "message_id": event["message_id"],
        }))

    @database_sync_to_async
    def save_message(self, room_id, sender_id, message):
        room = ChatRoom.objects.get(id=room_id)
        sender = User.objects.get(id=sender_id)

        return Message.objects.create(
            room=room,
            sender=sender,
            text=message
        )