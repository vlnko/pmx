from django import forms
from django.forms import ModelForm
from .models import Project, Task


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'category', 'description', 'deadline', 'head', 'project_team']


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'date_start', 'date_end', 'executor', 'work_hours_plan', 'work_hours_fact']
