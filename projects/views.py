from django.shortcuts import render, redirect
from django.views.generic import ListView
from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/projects_list.html"
