from django.db import models
from django.conf import settings 

class Room(models.Model):
    ROOM_TYPES = (
        ('private','Private'),
        ('group','Group'),
    )

    name = models.CharField(max_length=20, blank=True, unique=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='rooms')
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES, default='group')
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        if self.room_type == "private":
            return f"private chat ({', '.join([u.username for u in self.participants.all()])})"
        return self.name or f"Group {self.id}"
