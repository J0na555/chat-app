from django.urls import path
from .views import RoomListCreateView

app_name = 'rooms'

urlpatterns = [
    path('', RoomListCreateView.as_view(), name='rooms'),
]
