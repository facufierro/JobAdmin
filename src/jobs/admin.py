from django.contrib import admin

# Register your models here.

from .models import job, job_type

admin.site.register(job)
admin.site.register(job_type)
