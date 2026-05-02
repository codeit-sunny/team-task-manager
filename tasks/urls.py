from django.urls import path
from .views import create_task, task_list
from .views import create_task, task_list, update_task_status,task_api

urlpatterns = [
    path('create/', create_task, name='create_task'),
    path('list/', task_list, name='task_list'),
    path('update/<int:task_id>/', update_task_status, name='update_task'),
    path('api/', task_api, name='task_api'),
]