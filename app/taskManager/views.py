from django.shortcuts import render
from .models import Task


# Create your views here.
def home(requests):
    items = Task.objects.all()
    return render(requests, 'tasks.html', {"tasks": items})
