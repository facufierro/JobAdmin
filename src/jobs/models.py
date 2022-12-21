from django.db import models
from authentication.models import custom_user


class job_type(models.Model):
    id = models.AutoField(primary_key=True)
    job_type = models.CharField(max_length=100)

    def __str__(self):
        return self.job_type


class job(models.Model):
    id = models.AutoField(primary_key=True)
    job_type = models.ForeignKey(job_type, on_delete=models.CASCADE)
    users = models.ManyToManyField(custom_user, through="job_user")
    job_name = models.CharField(max_length=100)
    job_description = models.CharField(max_length=1000)
    job_location = models.CharField(max_length=100)

    def __str__(self):
        return self.job_name


class job_user(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.ForeignKey(job, on_delete=models.CASCADE)
    user = models.ForeignKey(custom_user, on_delete=models.CASCADE)
    rate = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.user.username


class worked_hour(models.Model):
    id = models.AutoField(primary_key=True)
    job_user = models.ForeignKey(job_user, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.job_user.user.username
