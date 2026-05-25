from django.urls import path
from .views import StartChatView, MessageListView
from .models import ChatRoom


def get_or_create_room(user, provider, booking_id):
    room, created = ChatRoom.objects.get_or_create(
        user=user,
        provider=provider,
        booking_id=booking_id
    )
    return room


urlpatterns = [
    path("start/", StartChatView.as_view()),
    path("messages/<int:room_id>/", MessageListView.as_view()),
]