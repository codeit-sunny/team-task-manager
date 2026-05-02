from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='project_members')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
