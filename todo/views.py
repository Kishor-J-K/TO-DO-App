from django.shortcuts import redirect, render
from django.http import HttpResponse
from todo.models import Task
def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'home.html', context)

def add_task(request):
    task = request.POST['task_name']
    Task.objects.create(task_name=task)
    return redirect('home')

def mark_as_done(request, id):
    task = Task.objects.get(id=id)
    task.is_completed = True
    task.save()
    return redirect('home')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')

def edit_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.task_name = request.POST['task_name']
        task.save()
        return redirect('home')
    context = {
        'task': task
    }
    return render(request, 'edit_task.html', context)

def mark_as_undone(request, id):
    task = Task.objects.get(id=id)
    task.is_completed = False
    task.save()
    return redirect('home')