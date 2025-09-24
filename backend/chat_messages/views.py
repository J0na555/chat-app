from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializer import MessageSerializer



class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.select_related('user', 'room')
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]