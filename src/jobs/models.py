from django.db import models
from users.models import custom_user


class job_type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class job(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    job_type_id = models.ForeignKey(job_type, on_delete=models.CASCADE)
    users = models.ManyToManyField(custom_user)

    def __str__(self):
        return self.name
