from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Room
from chat_messages.serializer import MessageSerializer
from .serializer import RoomSerializer

class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

class ChatDetail(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return Room.objects.filter(room__id=room_id).select_related('user', 'room')
