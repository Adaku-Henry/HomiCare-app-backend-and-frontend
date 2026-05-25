from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ChatRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_rooms")
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="provider_rooms")
    booking_id = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'provider', 'booking_id')

    def __str__(self):
        return f"Room {self.id}"


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField(blank=True)
    image = models.ImageField(upload_to="chat_images/", null=True, blank=True)

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.text[:20]}"