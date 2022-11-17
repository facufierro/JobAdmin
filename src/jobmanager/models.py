from django.db import models


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
