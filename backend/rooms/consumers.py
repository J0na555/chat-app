import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from chat_messages.models import Message
from rooms.models import Room
from chat_messages.serializers import MessageSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_id}'

        # Authenticate user using JWT
        user = await self.get_user_from_jwt()
        if not user:
            await self.close()
            return

        self.user = user

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        text = text_data_json['text']

        # Save message to database
        message = await self.save_message(text)

        # Serialize message
        serializer = MessageSerializer(message)
        message_data = serializer.data

        # Broadcast to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_data
            }
        )

    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))

    @database_sync_to_async
    def get_user_from_jwt(self):
        try:
            token = self.scope['query_string'].decode().split('token=')[1]
            jwt_auth = JWTAuthentication()
            validated_token = jwt_auth.get_validated_token(token)
            user = jwt_auth.get_user(validated_token)
            return user
        except (IndexError, Exception):
            return None

    @database_sync_to_async
    def save_message(self, text):
        room = Room.objects.get(id=self.room_id)
        return Message.objects.create(
            text=text,
            user=self.user,
            room=room
        )
# Async Consumer: Uses AsyncWebsocketConsumer for async WebSocket handling.
# Connect: Extracts room_id from URL, authenticates user via JWT (passed as ?token=<jwt>), joins a room group (chat_<room_id>).
# Disconnect: Leaves the room group.
# Receive: Parses incoming JSON ({"text": "Hello"}), saves the message to the database, serializes it, and broadcasts to the group.
# Chat Message: Sends the serialized message to connected clients.
# JWT Auth: Extracts token from query string and validates it.
# Save Message: Saves the message to the Message model asynchronously.