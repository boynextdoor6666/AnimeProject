from django.shortcuts import render

def index(request):
    return render (request, 'web_app/index.html')

def plot(request):
    return render (request, 'web_app/plot.html')

def characters(request):
    return render (request, 'web_app/characters.html')