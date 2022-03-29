from django.db import models
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse_lazy


USER_MODEL = settings.AUTH_USER_MODEL

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    members = models.ManyToManyField(USER_MODEL, related_name="projects")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("show_project", kwargs={"pk": self.pk})
