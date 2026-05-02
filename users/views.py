from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from django.http import HttpResponse
from .models import UserProfile
from tasks.models import Task
from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def dashboard_api(request):
    if request.user.userprofile.role == 'admin':
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assigned_to=request.user)

    data = {
        'total_tasks': tasks.count(),
        'completed_tasks': tasks.filter(status='done').count(),
        'pending_tasks': tasks.exclude(status='done').count(),
    }

    return Response(data)

def is_admin(user):
    return user.userprofile.role == 'admin'

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            UserProfile.objects.create(
                user=user,
                role=form.cleaned_data['role']
            )

            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()

    return render(request, 'users/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    if request.user.userprofile.role == 'admin':
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assigned_to=request.user)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='done').count()
    pending_tasks = tasks.exclude(status='done').count()
    overdue_tasks = tasks.filter(due_date__lt=date.today()).exclude(status='done').count()

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'overdue_tasks': overdue_tasks,
    }

    return render(request, 'users/dashboard.html', context)




