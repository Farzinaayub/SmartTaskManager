from django.db import models

# Create your models here.


class Task(models.Model):
    Id = models.CharField(max_length=200)
    Action = models.CharField(max_length=200)
    Task = models.CharField(max_length=200, null=True)
    Time = models.CharField(max_length=200, null=True)
    Relative_time = models.CharField(max_length=200, null=True)
    stakeholders = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200)
    priority = models.CharField(max_length=200)

    def __str__(self):
        return self.name
