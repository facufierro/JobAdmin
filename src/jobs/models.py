from django.db import models

# import customuser
from authentication.models import CustomUser

# Create your models here.


class JobType(models.Model):
    id = models.AutoField(primary_key=True)
    job_type = models.CharField(max_length=100)

    def __str__(self):
        return self.job_type


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class WorkedHour(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.employee.name + " - " + self.job.title + " - " + str(self.hours)
