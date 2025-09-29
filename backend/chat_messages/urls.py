from django.urls import path
from .views import MessageListCreateView

app_name = 'chat_messages'

urlpatterns = [
    path('', MessageListCreateView.as_view(), name='messages'),
]