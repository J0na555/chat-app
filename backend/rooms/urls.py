from django.urls import path
from .views import RoomListCreateView, ChatDetail

app_name = 'rooms'

urlpatterns = [
    path('', RoomListCreateView.as_view(), name='rooms'),
    path('<int:room_id>/messages/', ChatDetail.as_view(), name='room_messages'),
]
