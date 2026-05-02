from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer


@api_view(['GET'])
def task_api(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

def create_task(request):
    if request.user.userprofile.role != 'admin':
        return HttpResponse("Access Denied")

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('task_list')
        else:
            print(form.errors)

    else:
        form = TaskForm()

    return render(request, 'tasks/create_task.html', {'form': form})


def task_list(request):
    if request.user.userprofile.role == 'admin':
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assigned_to=request.user)

    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def update_task_status(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.user != task.assigned_to:
        return HttpResponse("Access Denied")

    if request.method == 'POST':
        task.status = request.POST['status']
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/update_task.html', {'task': task})