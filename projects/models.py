from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=150)
    owner = models.ForeignKey(
        User,
        related_name="projects",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name
