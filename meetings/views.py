from django.shortcuts import render
from .models import Meeting
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


class MeetingListView(LoginRequiredMixin, ListView):
    model = Meeting
    context_object_name = 'meetings'
    ordering = '-date'