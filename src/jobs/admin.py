from django.contrib import admin

# Register your models here.

from .models import Job, JobType, WorkedHour

admin.site.register(Job)
admin.site.register(JobType)
admin.site.register(WorkedHour)
