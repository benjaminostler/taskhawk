from django.shortcuts import render
from projects.models import Project


def list_projects(request):
    list_projects = Project.objects.all()
    context = {
        "list_projects": list_projects,
    }
    return render(request, "projects/projects.html", context)
