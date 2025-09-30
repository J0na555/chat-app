from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Room
from chat_messages.serializers import MessageSerializer
from .serializers import RoomSerializer

class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


class RoomListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.all()

class RoomDetailView(generics.RetrieveAPIView):
    permission_class = [IsAuthenticated]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    lookup_field = 'id'
    


class ChatDetail(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return Room.objects.filter(room__id=room_id).select_related('user', 'room')
