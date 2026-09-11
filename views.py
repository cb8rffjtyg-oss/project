from django.shortcuts import render
from .models import Task

def home(request):
    tasks = Task.objects.all()
    
    context = {
        'title': 'مشروع Lab 2 & 3',
        'items': ['DTL Variables', 'DTL Filters', 'CSS Static Files', 'Database Integration'],
        'tasks': tasks
    }
    return render(request, 'myapp/index.html', context)