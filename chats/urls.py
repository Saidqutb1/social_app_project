from django.urls import path
from .views import search_users, chat_view, chat_list

app_name = 'chats'

urlpatterns = [
    path('search/', search_users, name='search_users'),
    path('chat/<int:user_id>/', chat_view, name='chat_view'),
    path('list/', chat_list, name='chat_list'),
]
