from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from projects.models import Project
from tasks.models import Task
from projects.forms import ProjectForm
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


@login_required
def create_project(request):
    # Check if request is a POST
    if request.method == "POST":
        # Create new form instance & fill with values from submission
        form = ProjectForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # save all info from form into variable
            project = form.save(False)
            # add logged in user as the purchaser attribute in project
            project.owner = request.user
            # Save project with user info
            project.save()
        # Redirect to a different page
        return redirect("list_projects")
    else:
        # Create a new form instance
        form = ProjectForm()
    # Add it to the context
    context = {"form": form}
    return render(request, "projects/create.html", context)
