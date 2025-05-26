from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        # Verificar si es para crear tarea o cambiar estado
        if 'toggle_task' in request.POST:
            task_id = request.POST.get('task_id')
            task = Task.objects.get(id=task_id)
            task.is_completed = not task.is_completed
            task.save()
            return redirect('Home')
        
        # Crear nueva tarea
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = TaskForm()

    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks.html', {'tasks': tasks, 'form': form})
