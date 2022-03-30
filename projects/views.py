from django.views.generic import ListView, DetailView, CreateView
from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task


# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/projects_list.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        return context


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/projects_detail.html"
    # context_object_name = "project_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/projects_create.html"
    fields = ["name", "description", "members"]
