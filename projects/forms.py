from django import forms
from django.forms.widgets import NumberInput
from django.forms import ModelForm
from .models import Project, Task


class ProjectCreateForm(ModelForm):
    deadline = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Project
        fields = ['title', 'category', 'description', 'deadline', 'head', 'project_team']


class ProjectUpdateForm(ModelForm):
    deadline = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Project
        fields = ['title', 'category', 'description', 'deadline', 'head', 'project_team']


class TaskCreateForm(ModelForm):
    date_start = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    date_end = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'date_start', 'date_end', 'executor', 'work_hours_plan', 'work_hours_fact']


class TaskUpdateForm(ModelForm):
    date_start = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    date_end = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'status', 'date_start', 'date_end', 'executor', 'work_hours_plan', 'work_hours_fact']
