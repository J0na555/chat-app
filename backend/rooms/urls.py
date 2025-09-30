from django.urls import path
from .views import RoomListCreateView, ChatDetail, RoomListView, RoomDetailView, RoomDeleteView, RoomUpdateView

app_name = 'rooms'

urlpatterns = [
    path('', RoomListCreateView.as_view(), name='rooms'),
    path('<int:room_id>/messages/', ChatDetail.as_view(), name='room-messages'),
    path('list/', RoomListView.as_view(), name='room-list'),
    path('<int:id>/', RoomDetailView.as_view(), name= "room-detail"),
    path('<int:id>/delete/', RoomDeleteView.as_view(), name= "room-delete"),
    path('<int:id>/update/', RoomUpdateView.as_view(), name="room-update"),
]
