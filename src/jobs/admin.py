from django.contrib import admin

# Register your models here.

from .models import job, job_type, job_user, worked_hour

admin.site.register(job)
admin.site.register(job_type)
admin.site.register(job_user)
admin.site.register(worked_hour)
