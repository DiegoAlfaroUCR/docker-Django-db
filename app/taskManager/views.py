from django.shortcuts import render
from .models import Task


# Create your views here.
def home(requests):
    items = Task.objects.all()
    render(requests, 'tasks.html', items)
