# myapp/views/your_views.py

from django.shortcuts import render
from pywebio import start_server



from .import main


def chat_view(request):


    if __name__ == "__main__":
        start_server(main, debug=True, host='0.0.0.0', port=8080, cdn=False)

# chat/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)


    def get_full_name(self):

        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):

        return self.username

    def __str__(self):

        return self.get_full_name()


# chat/models.py

from django.db import models
from django.contrib.auth import get_user_model

class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver} - {self.timestamp}"

from chat.models import Message


