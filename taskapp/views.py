from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DeleteView, UpdateView


def task_list(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    tasks = Task._default_manager.order_by("-created_at")
    return render(request, "taskapp/task_list.html", {"form": form, "tasks": tasks})


# def complete_task(request, pk):
#     if request.method == "POST":
#         task = get_object_or_404(Task, pk=pk)
#         task.completed = True
#         task.save()
#     return redirect("task_list")


class TaskCompleteView(UpdateView):
    model = Task
    fields = ["completed"]

    def post(self, request, pk):
        task = self.get_object()
        task.completed = True
        task.save()
        return redirect("task_list")


# def delete_task(request, pk):
#     if request.method == "POST":
#         task = get_object_or_404(Task, pk=pk)
#         task.delete()
#     return redirect("task_list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = "/"
