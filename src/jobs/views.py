from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, TemplateView

# import mixin to check if user is logged in
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import job, job_type, worked_hour, job_user


class HomePageView(TemplateView):
    template_name = "base/home.html"


class AboutPageView(TemplateView):
    template_name = "base/about.html"


class JobIndexView(ListView, LoginRequiredMixin):
    model = job
    template_name = "jobs/job_index.html"
    context_object_name = "jobs"


class JobDetailView(DetailView, LoginRequiredMixin):
    model = job
    template_name = "jobs/detail.html"


class JobCreateView(CreateView, LoginRequiredMixin):
    model = job
    template_name = "jobs/create.html"
    fields = ["title", "description", "job_type"]
    success_url = reverse_lazy("job_index")


class JobUpdateView(UpdateView, LoginRequiredMixin):
    model = job
    template_name = "jobs/update.html"
    fields = ["title", "description", "job_type"]
    success_url = reverse_lazy("job_index")


class JobDeleteView(DeleteView, LoginRequiredMixin):
    model = job
    template_name = "jobs/delete.html"
    success_url = reverse_lazy("job_index")


class JobTypeIndexView(ListView, LoginRequiredMixin):
    model = job_type
    template_name = "jobs/job_index.html"


class JobTypeDetailView(DetailView, LoginRequiredMixin):
    model = job_type
    template_name = "jobs/detail.html"


class JobTypeCreateView(CreateView, LoginRequiredMixin):
    model = job_type
    template_name = "jobs/create.html"
    fields = ["job_type"]
    success_url = reverse_lazy("job_type_index")


class JobTypeUpdateView(UpdateView, LoginRequiredMixin):
    model = job_type
    template_name = "jobs/update.html"
    fields = ["job_type"]
    success_url = reverse_lazy("job_type_index")


class JobTypeDeleteView(DeleteView, LoginRequiredMixin):
    model = job_type
    template_name = "jobs/delete.html"
    success_url = reverse_lazy("job_type_index")
