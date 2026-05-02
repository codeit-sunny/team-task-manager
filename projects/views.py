from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer


@api_view(['GET'])
def project_api(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

def create_project(request):
    if request.user.userprofile.role != 'admin':
        return HttpResponse("Access Denied")

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            form.save_m2m()
            return redirect('project_list')
    else:
        form = ProjectForm()

    return render(request, 'projects/create_project.html', {'form': form})


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})
