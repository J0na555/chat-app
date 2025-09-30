from django.urls import path
from .views import RoomListCreateView, ChatDetail, RoomListView, RoomDetailView

app_name = 'rooms'

urlpatterns = [
    path('', RoomListCreateView.as_view(), name='rooms'),
    path('<int:room_id>/messages/', ChatDetail.as_view(), name='room_messages'),
    path('list/', RoomListView.as_view(), name='room_list'),
    path('<int:id>/', RoomDetailView.as_view(), name= "room_detail"),
]
