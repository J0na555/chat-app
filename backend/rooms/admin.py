from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_participants", "created_at")

    def get_participants(self, obj):
        return ", ".join([u.username for u in obj.participants.all()])
    get_participants.short_description = "participants"
