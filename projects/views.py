from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project


from .forms import ProjectCreateForm


class ProjectCreateView(LoginRequiredMixin, CreateView):
    form_class = ProjectCreateForm
    success_url = reverse_lazy("project-all")
    template_name = "projects/projectcreate.html"


class ProjectList(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projects'