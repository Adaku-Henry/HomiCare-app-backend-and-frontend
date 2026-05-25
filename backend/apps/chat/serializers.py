from rest_framework import serializers
from .models import Message, ChatRoom


class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(
        source="sender.username",
        read_only=True
    )

    class Meta:
        model = Message
        fields = "__all__"


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = "__all__"