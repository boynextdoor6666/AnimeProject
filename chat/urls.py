# chat/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import chat_view, SignupView

urlpatterns = [
    path('', chat_view, name='chat'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]


