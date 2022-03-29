from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/tasks_create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    # def form_valid(self, form):
    #     item = form.save(commit=False)
    #     item.assignee = self.request.user
    #     item.save()
    #     form.save_m2m()
    #     return redirect("show_project", pk=item.id)
