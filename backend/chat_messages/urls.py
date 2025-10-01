from django.urls import path
from .views import MessageListCreateView, GetMessages, DeleteMessagesView, UpdateMessagesView

app_name = 'chat_messages'

urlpatterns = [
    path('', MessageListCreateView.as_view(), name='messages'),
    path('list/<int:room_id>/', GetMessages.as_view(), name='message-list'),
    path('<int:id>/update/', UpdateMessagesView.as_view(), name='update-message'),
    path('<int:id>/delete/', DeleteMessagesView.as_view(), name='delete-message'),
]