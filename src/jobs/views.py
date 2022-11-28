from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, TemplateView

from django.urls import reverse_lazy
from .models import Job, JobType, Employee, WorkedHours


class HomePageView(TemplateView):
    template_name = 'base/home.html'


class AboutPageView(TemplateView):
    template_name = 'base/about.html'


class JobIndexView(ListView):
    model = Job
    template_name = 'jobs/index.html'
    context_object_name = 'jobs'


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/detail.html'


class JobCreateView(CreateView):
    model = Job
    template_name = 'jobs/create.html'
    fields = ['title', 'description', 'job_type']
    success_url = reverse_lazy('job_index')


class JobUpdateView(UpdateView):
    model = Job
    template_name = 'jobs/update.html'
    fields = ['title', 'description', 'job_type']
    success_url = reverse_lazy('job_index')


class JobDeleteView(DeleteView):
    model = Job
    template_name = 'jobs/delete.html'
    success_url = reverse_lazy('job_index')


class JobTypeIndexView(ListView):
    model = JobType
    template_name = 'jobs/index.html'


class JobTypeDetailView(DetailView):
    model = JobType
    template_name = 'jobs/detail.html'


class JobTypeCreateView(CreateView):
    model = JobType
    template_name = 'jobs/create.html'
    fields = ['job_type']
    success_url = reverse_lazy('job_type_index')


class JobTypeUpdateView(UpdateView):
    model = JobType
    template_name = 'jobs/update.html'
    fields = ['job_type']
    success_url = reverse_lazy('job_type_index')


class JobTypeDeleteView(DeleteView):
    model = JobType
    template_name = 'jobs/delete.html'
    success_url = reverse_lazy('job_type_index')


class EmployeeIndexView(ListView):
    model = Employee
    template_name = 'jobs/index.html'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'jobs/detail.html'


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'jobs/create.html'
    fields = ['name', 'email', 'phone', 'address']
    success_url = reverse_lazy('employee_index')


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'jobs/update.html'
    fields = ['name', 'email', 'phone', 'address']
    success_url = reverse_lazy('employee_index')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'jobs/delete.html'
    success_url = reverse_lazy('employee_index')


class WorkedHoursIndexView(ListView):
    model = WorkedHours
    template_name = 'worked_hours/index.html'


class WorkedHoursDetailView(DetailView):
    model = WorkedHours
    template_name = 'worked_hours/detail.html'


class WorkedHoursCreateView(CreateView):
    model = WorkedHours
    template_name = 'worked_hours/create.html'
    fields = ['employee', 'job', 'start_time', 'end_time']
    success_url = reverse_lazy('worked_hours_index')


class WorkedHoursUpdateView(UpdateView):
    model = WorkedHours
    template_name = 'worked_hours/update.html'
    fields = ['employee', 'job', 'start_time', 'end_time']
    success_url = reverse_lazy('worked_hours_index')


class WorkedHoursDeleteView(DeleteView):
    model = WorkedHours
    template_name = 'worked_hours/delete.html'
    success_url = reverse_lazy('worked_hours_index')
