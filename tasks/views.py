from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task
from django.urls import reverse_lazy

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/tasks_create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/tasks_list.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/tasks_update.html"
    fields = ["is_completed"]

    success_url = reverse_lazy("show_my_tasks")
