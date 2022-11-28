from django.contrib import admin

# Register your models here.

from .models import Job, JobType, Employee, WorkedHours

admin.site.register(Job)
admin.site.register(JobType)
admin.site.register(Employee)
admin.site.register(WorkedHours)
