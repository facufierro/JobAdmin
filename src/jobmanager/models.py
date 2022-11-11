from django.db import models

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    salary = models.IntegerField()
    company = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=1000)
    employee_number = models.IntegerField()
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name