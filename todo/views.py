from django.shortcuts import render
from todo.models import Task
def home(request):
    task = Task.objects.filter(is_completed=False).order_by('-created_at')
    completed_task = Task.objects.filter(is_completed=True).order_by('-updated_at')
    return render(request, 'home.html', {'tasks': task, 'completed_tasks': completed_task})