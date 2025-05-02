from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, TaskStatusForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todos/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todos/create_task.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskStatusForm
from .models import Task

def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskStatusForm(request.POST)
        if form.is_valid():
            task.status = form.cleaned_data['status']
            task.save()
            return redirect('task_list')
    else:
        form = TaskStatusForm(initial={'status': task.status})
    return render(request, 'todos/update_task_status.html', {'task': task, 'form': form})



def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task_list')

def home(request):
    return render(request, 'todos/home.html')
