from django.shortcuts import (
    render,
    get_object_or_404,
    get_list_or_404,
    redirect,
)
from tasks.models import Task
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required


@login_required
def create_task(request):
    # Check if request is a POST
    if request.method == "POST":
        # Create new form instance & fill with values from submission
        form = TaskForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save receipt
            form.save
        # Redirect to a different page
        return redirect("show_my_tasks")
    else:
        # Create a new form instance
        form = TaskForm()
    # Add it to the context
    context = {"form": form}
    return render(request, "tasks/create.html", context)


@login_required
def show_my_tasks(request):
    list_tasks = Task.objects.filter(assignee=request.user)
    context = {
        "list_tasks": list_tasks,
    }
    return render(request, "tasks/mine.html", context)
