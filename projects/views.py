from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import ProjectCreateForm


class ProjectCreateView(LoginRequiredMixin, CreateView):
    form_class = ProjectCreateForm
    success_url = reverse_lazy("home")
    template_name = "projects/projectcreate.html"