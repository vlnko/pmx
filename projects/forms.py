from django import forms
from django.forms import ModelForm
from .models import Project


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'category', 'description', 'head', 'project_team']