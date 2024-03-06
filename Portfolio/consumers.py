from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.db.models import Q
from users_chat.models import CustomUser, Rooms, Message


class ChatConsumer(AsyncWebsocketConsumer):
    connected_users = set()

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_slug']
        self.room_group_name = await self.get_room_name()

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept connection
        await self.accept()

        # Add current channel name to connected_users set
        self.connected_users.add(self.channel_name)
        room_members = len(self.connected_users)

        # Send a message when connection is established
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "send_message",
                "status": "Online",
                "online_members": room_members,
            }
        )

    async def disconnect(self, close_code):
        # Remove current channel name from connected_users set
        self.connected_users.remove(self.channel_name)
        room_members = len(self.connected_users)

        # Send a message when connection is closed
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "send_message",
                "status": "Offline",
                "online_members": room_members,
            }
        )

        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        # Receive message from WebSocket
        # In this example, we're not doing anything with received messages
        pass

    @sync_to_async
    def get_room_name(self):
        room = Rooms.objects.filter(slug=self.room_name).first()
        print(self.room_name, '------------')
        print(room, ")))))))))))))))))))))))))")
        return room.name if room else None

    async def send_message(self, event):
        status = event['status']
        online_members = event['online_members']

        # Send message to WebSocket
        await self.send(text_data=f"Status: {status}, Online Members: {online_members}")
