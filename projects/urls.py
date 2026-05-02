from django.urls import path
from .views import create_project, project_list,project_api

urlpatterns = [
    path('create/', create_project, name='create_project'),
    path('list/', project_list, name='project_list'),
    path('api/', project_api, name='project_api'),
]