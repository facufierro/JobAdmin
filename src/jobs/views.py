from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, TemplateView

# import mixin to check if user is logged in
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import job, job_type


class HomePageView(TemplateView):
    template_name = "base/home.html"


class AboutPageView(TemplateView):
    template_name = "base/about.html"


class JobIndexView(ListView):
    model = job
    template_name = "jobs/job_index.html"
    context_object_name = "jobs"


class JobDetailView(DetailView):
    model = job
    template_name = "jobs/job_detail.html"
    context_object_name = "job"


class JobCreateView(LoginRequiredMixin, CreateView):
    model = job
    template_name = "jobs/job_create.html"
    fields = ["name", "description", "start_date", "end_date", "job_type_id", "users"]
    success_url = reverse_lazy("job_index")


class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = job
    template_name = "jobs/job_edit.html"
    fields = ["name", "description", "start_date", "end_date", "job_type_id", "users"]
    success_url = reverse_lazy("job_index")


class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = job
    template_name = "jobs/job_delete.html"
    context_object_name = "job"
    success_url = reverse_lazy("job_index")


class JobTypeIndexView(ListView):
    model = job_type
    template_name = "jobs/job_index.html"
    context_object_name = "job_types"


class JobTypeDetailView(DetailView):
    model = job_type
    template_name = "jobs/job_detail.html"
    context_object_name = "job_type"


class JobTypeCreateView(LoginRequiredMixin, CreateView):
    model = job_type
    template_name = "jobs/job_create.html"
    fields = ["name"]
    success_url = reverse_lazy("job_index")


class JobTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = job_type
    template_name = "jobs/job_edit.html"
    fields = ["name"]
    success_url = reverse_lazy("job_index")


class JobTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = job_type
    template_name = "jobs/job_delete.html"
    context_object_name = "job_type"
    success_url = reverse_lazy("job_index")
