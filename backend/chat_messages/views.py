from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Message
from rooms.models import Room
from .serializers import MessageSerializer



class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.select_related('user', 'room')
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
        
    

class GetMessages(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return Message.objects.filter(room_id=room_id)