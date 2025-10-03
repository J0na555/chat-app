from django.urls import path

def get_websocket_urlpatterns():
    from .consumers import ChatConsumer
    return [
        path('ws/rooms/<int:room_id>/', ChatConsumer.as_asgi()),
    ]
