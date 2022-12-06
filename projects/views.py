from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project, Task
from .forms import ProjectCreateForm, TaskCreateForm
from django.http import HttpResponseRedirect


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


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy("project-all")
    template_name = "projects/project_delete.html"


class TaskCreateView(LoginRequiredMixin, CreateView):
    form_class = TaskCreateForm
    template_name = "projects/task_create.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.fcc_form = form.save(commit=True)
            return HttpResponseRedirect(reverse_lazy('project-detail', kwargs={'pk': self.fcc_form.project.id}))
        else:
            return render(request, self.template_name, {'form': form})


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "projects/task_detail.html"


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['project', 'title', 'status', 'description', 'date_start', 'date_end', 'executor', 'work_hours_plan', 'work_hours_fact']    
    template_name = "projects/task_update.html"

    def get_success_url(self):
       pk = self.kwargs["pk"]
       return reverse_lazy("task-detail", kwargs={"pk": pk})
    
    def form_valid(self, form):
        return super(TaskUpdateView,self).form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    # success_url = reverse_lazy('project-all')
    template_name = "projects/task_delete.html"

    def get_success_url(self):
       pk = self.object.project.id
       return reverse_lazy("project-detail", kwargs={"pk": pk})