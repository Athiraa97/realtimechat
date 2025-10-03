import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # single group name used for broadcasting notifications
        self.group_name = "global_notifications"
        # add this connection to the group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # remove from group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # Receive message from WebSocket (sender will send here)
    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
        except Exception:
            # ignore malformed
            return
        message = data.get("message", "")
        # Broadcast to group
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "broadcast_notification",
                "message": message,
            }
        )

    # Called by channel_layer.group_send
    async def broadcast_notification(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"]
        }))
