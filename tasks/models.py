from django.db import models

from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Task(models.Model):
    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    due_date = models.DateField()

    def __str__(self):
        return self.title
