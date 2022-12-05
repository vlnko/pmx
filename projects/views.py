from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .forms import ProjectCreateForm


class ProjectCreateView(LoginRequiredMixin, CreateView):
    form_class = ProjectCreateForm
    success_url = reverse_lazy("project-all")
    template_name = "projects/project_create.html"


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projects'
    queryset = Project.objects.all().prefetch_related('task_set').all()


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['title', 'category', 'description', 'deadline', 'head', 'project_team']
    success_url = reverse_lazy("project-all")
    template_name = "projects/project_update.html"

    def form_valid(self, form):
        return super(ProjectUpdateView,self).form_valid(form)