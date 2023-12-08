# myapp/views/your_views.py

from django.shortcuts import render
from pywebio import start_server

from myapp.chat.your_chat_script import main

def chat_view(request):


    if __name__ == "__main__":
        start_server(main, debug=True, host='0.0.0.0', port=8080, cdn=False)
