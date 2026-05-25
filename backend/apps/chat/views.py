from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import ChatRoom, Message
from .serializers import MessageSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class StartChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        other_user_id = request.data.get("user_id")

        other_user = User.objects.get(id=other_user_id)

        room = ChatRoom.objects.create()

        room.participants.add(request.user)
        room.participants.add(other_user)

        return Response({
            "room_id": room.id
        })


class MessageListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, room_id):
        messages = Message.objects.filter(
            room_id=room_id
        ).order_by("created_at")

        serializer = MessageSerializer(messages, many=True)

        return Response(serializer.data)