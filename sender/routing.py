# Sender does not need to listen for group messages in this example,
# but we keep routing if you want the sender to also open websockets.
from django.urls import path

websocket_urlpatterns = [
    # (none needed for sender in this demo)
]
        