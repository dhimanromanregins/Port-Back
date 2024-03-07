from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.db.models import Q
from users_chat.models import CustomUser, Rooms, Message
import json


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
                "type": "sendMessage",
                "status": "Online",
                "online_members": room_members,
            }
        )

    async def disconnect(self, close_code):
        # Remove current channel name from connected_users set
        self.connected_users.remove(self.channel_name)
        self.room_members = len(self.connected_users)

        # Send a message when connection is closed
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "sendMessage",
                "status": "Offline",
                "online_members": self.room_members,
            }
        )

        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json.get('sender_username'):
            message = text_data_json['message']
            sender_username = text_data_json["sender_username"]
            print("0000000000000000")
            await self.save_message(message, sender_username)
            message = text_data_json
            await self.channel_layer.group_send(
                self.room_group_name, {
                    "type": "sendMessage",  # Corrected message type here
                    "message": message,
                    "username": sender_username,
                    "room_name": self.room_group_name,
                }
            )
        # elif text_data_json.get('typing_status'):
        #     message = text_data_json
        #     await self.channel_layer.group_send(
        #         self.roomGroupName, {
        #             "type": "sendMessage",
        #             "message": message,
        #         }
        #     )


    @sync_to_async
    def get_room_name(self):
        room = Rooms.objects.filter(slug=self.room_name).first()
        return room.name if room else None

    async def sendMessage(self, event):
        message = event.get("message")
        if event.get("status"):
            await self.send(text_data=json.dumps({"status": event.get("status"), "online_members": event.get("online_members")}))
        else:
            await self.send(text_data=json.dumps(message))

    @sync_to_async
    def save_message(self, message, sender_username):
        print("00000000000000000000000")
        try:
            room = Rooms.objects.get(name=self.room_group_name)
            sender_user = CustomUser.objects.get(username=sender_username)
            Message.objects.create(sender_username=sender_user, room=room, content=message)
        except CustomUser.DoesNotExist:
            print('Error: User with username "{}" does not exist.'.format(sender_username))
        except Exception as err:
            print('Error while saving message -', err)