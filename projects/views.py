from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .forms import ProjectCreateForm


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/project_detail.html"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    form_class = ProjectCreateForm
    success_url = reverse_lazy("project-all")
    template_name = "projects/project_create.html"


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projects'


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['title', 'category', 'description', 'deadline', 'head', 'project_team']
    template_name = "projects/project_update.html"

    def get_success_url(self):
       pk = self.kwargs["pk"]
       return reverse_lazy("project-detail", kwargs={"pk": pk})

    def form_valid(self, form):
        return super(ProjectUpdateView,self).form_valid(form)