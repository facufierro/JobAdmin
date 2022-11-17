from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, TemplateView

from django.urls import reverse_lazy
from .models import Job, JobType


class HomePageView(TemplateView):
    template_name = 'base/home.html'