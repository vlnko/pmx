from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Project views

@login_required(login_url='login')
def DashboardView(request):
    my_tasks = Task.objects.all().filter(
        executor=request.user).order_by('status', 'date_end')
    return render(request, 'projects/home.html', {'title': 'PMX: Дашборд', 'tasks': my_tasks})


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
    ordering = 'deadline'


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = "projects/project_update.html"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("project-detail", kwargs={"pk": pk})

    def form_valid(self, form):
        return super(ProjectUpdateView, self).form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy("project-all")
    template_name = "projects/project_delete.html"


# Task views

class TaskCreateView(LoginRequiredMixin, CreateView):
    form_class = TaskCreateForm
    template_name = "projects/task_create.html"

    def get(self, request, pr_id):
        form = self.form_class(initial={'project': pr_id, 'executor': request.user})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.fcc_form = form.save(commit=True)
            return HttpResponseRedirect(reverse_lazy('project-detail', kwargs={'pk': self.fcc_form.project.id}))
        else:
            return render(request, self.template_name, {'form': form})


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = "projects/task_update.html"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("project-home")

    def form_valid(self, form):
        return super(TaskUpdateView, self).form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "projects/task_delete.html"

    def get_success_url(self):
        pk = self.object.project.id
        return reverse_lazy("project-detail", kwargs={"pk": pk})


@login_required(login_url='login')
def MyTasksView(request): # actually returns all tasks
    tasks = Task.objects.all().order_by('status', 'date_end')
    return render(request, 'projects/task_my_list.html', {'title': 'My tasks', 'tasks': tasks})


# Functions setting task statuses

@login_required(login_url='login')
def TaskMakeInboxView(request, pk): # makes status inbox
    task = Task.objects.get(id=pk)
    task.status = "AI"
    task.save()
    return HttpResponseRedirect(reverse_lazy('get-tasks'))


@login_required(login_url='login')
def TaskMakeWorkingView(request, pk): # makes status working
    task = Task.objects.get(id=pk)
    task.status = "BW"
    task.save()
    return HttpResponseRedirect(reverse_lazy('get-tasks'))


@login_required(login_url='login')
def TaskMakeCheckingView(request, pk): # makes status checking
    task = Task.objects.get(id=pk)
    task.status = "CC"
    task.save()
    return HttpResponseRedirect(reverse_lazy('get-tasks'))


@login_required(login_url='login')
def TaskMakeReworkingView(request, pk): # makes status reworking
    task = Task.objects.get(id=pk)
    task.status = "DR"
    task.save()
    return HttpResponseRedirect(reverse_lazy('get-tasks'))


@login_required(login_url='login')
def TaskMakeDoneView(request, pk): # makes status done
    task = Task.objects.get(id=pk)
    task.status = "ED"
    task.save()
    return HttpResponseRedirect(reverse_lazy('get-tasks'))


def getTasks(request): # gets all tasks for current user
    tasks = Task.objects.all().filter(
        executor=request.user).order_by('status', 'date_end')
    return render(request, 'projects/taskx.html', {'tasks': tasks})


# Utility views

def getMyProgress(request): # returns progress info for widget
    count_my_tasks_all = len(Task.objects.all().filter(executor=request.user))
    count_my_tasks_done = len(Task.objects.all().filter(
        executor=request.user).filter(status='ED'))
        
    if count_my_tasks_all > 0:
        my_progress = str(
            int(count_my_tasks_done / count_my_tasks_all * 100)) + '%'
    else:
        my_progress = 0

    return render(request, 'projects/progressx.html', {'progress': my_progress})
