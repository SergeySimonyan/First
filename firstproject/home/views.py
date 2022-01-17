from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'home/index.html', {'title': 'Site`s home page', 'tasks': tasks})

def about(request):
    return render(request, 'home/about.html')
