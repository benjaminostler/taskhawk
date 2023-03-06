from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required


@login_required
def list_projects(request):
    list_projects = Project.objects.filter(owner=request.user)
    context = {
        "list_projects": list_projects,
    }
    return render(request, "projects/projects.html", context)
