from django.shortcuts import (
    render,
    get_object_or_404,
    get_list_or_404,
    redirect,
)
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required


@login_required
def list_projects(request):
    list_projects = Project.objects.filter(owner=request.user)
    context = {
        "list_projects": list_projects,
    }
    return render(request, "projects/projects.html", context)


@login_required
def show_project(request, id):
    project_object = get_object_or_404(Project, id=id)
    task_list = Task.objects.filter(project=id)
    context = {
        "project_object": project_object,
        "task_list": task_list,
    }
    return render(request, "projects/detail.html", context)
