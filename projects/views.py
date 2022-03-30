from django.views.generic import ListView, DetailView, CreateView
from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/projects_list.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/projects_detail.html"
    context_object_name = "project_detail"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/projects_create.html"
    fields = ["name", "description", "members"]
