from django.urls import path
from .views import MessageListCreateView, GetMessages

app_name = 'chat_messages'

urlpatterns = [
    path('', MessageListCreateView.as_view(), name='messages'),
    path('list/<int:room_id>/', GetMessages.as_view(), name='message-list'),
]