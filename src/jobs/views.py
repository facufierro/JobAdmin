from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, TemplateView

from django.urls import reverse_lazy
from .models import Job, JobType, WorkedHour


class HomePageView(TemplateView):
    template_name = "base/home.html"


class AboutPageView(TemplateView):
    template_name = "base/about.html"


class JobIndexView(ListView):
    model = Job
    template_name = "jobs/job_index.html"
    context_object_name = "jobs"


class JobDetailView(DetailView):
    model = Job
    template_name = "jobs/detail.html"


class JobCreateView(CreateView):
    model = Job
    template_name = "jobs/create.html"
    fields = ["title", "description", "job_type"]
    success_url = reverse_lazy("job_index")


class JobUpdateView(UpdateView):
    model = Job
    template_name = "jobs/update.html"
    fields = ["title", "description", "job_type"]
    success_url = reverse_lazy("job_index")


class JobDeleteView(DeleteView):
    model = Job
    template_name = "jobs/delete.html"
    success_url = reverse_lazy("job_index")


class JobTypeIndexView(ListView):
    model = JobType
    template_name = "jobs/job_index.html"


class JobTypeDetailView(DetailView):
    model = JobType
    template_name = "jobs/detail.html"


class JobTypeCreateView(CreateView):
    model = JobType
    template_name = "jobs/create.html"
    fields = ["job_type"]
    success_url = reverse_lazy("job_type_index")


class JobTypeUpdateView(UpdateView):
    model = JobType
    template_name = "jobs/update.html"
    fields = ["job_type"]
    success_url = reverse_lazy("job_type_index")


class JobTypeDeleteView(DeleteView):
    model = JobType
    template_name = "jobs/delete.html"
    success_url = reverse_lazy("job_type_index")


class WorkedHourIndexView(ListView):
    model = WorkedHour
    template_name = "jobs/job_index.html"


class WorkedHourDetailView(DetailView):
    model = WorkedHour
    template_name = "jobs/detail.html"


class WorkedHourCreateView(CreateView):
    model = WorkedHour
    template_name = "jobs/create.html"
    fields = ["employee", "job", "hours_worked"]
    success_url = reverse_lazy("worked_hour_index")


class WorkedHourUpdateView(UpdateView):
    model = WorkedHour
    template_name = "jobs/update.html"
    fields = ["employee", "job", "hours_worked"]
    success_url = reverse_lazy("worked_hour_index")
