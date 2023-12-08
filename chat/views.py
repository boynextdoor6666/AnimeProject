# chat/views.py
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render  # Добавьте этот импорт
from .forms import CustomUserCreationForm

def chat_view(request):
    messages = []  # Подставьте свою логику получения сообщений
    return render(request, 'chat/chat.html', {'messages': messages})

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# chat/views.py
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def chat_view(request):
    messages = Message.objects.all()
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.user = request.user
            new_message.save()
            return redirect('chat')

    return render(request, 'chat/chat.html', {'messages': messages, 'form': form})


from django.shortcuts import render
from django.http import HttpResponse
from chat.main import main

def chat_view(request):

    main()
    return HttpResponse("Chat server is running.")


