from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    description = models.TextField()
    job_type = models.ForeignKey('JobType', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class JobType(models.Model):
    id = models.AutoField(primary_key=True)
    job_type = models.CharField(max_length=100)

    def __str__(self):
        return self.job_type


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class JobEmployee(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    def __str__(self):
        return self.job.title + ' - ' + self.employee.name