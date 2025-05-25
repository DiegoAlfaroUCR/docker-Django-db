from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = TaskForm()

    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks.html', {'tasks': tasks, 'form': form})
