from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','name' 'participants', 'room_type', 'created_at']
        read_only_fields = ('id', 'created_at')