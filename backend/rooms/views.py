from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Room
from .serializer import RoomSerializer

class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]