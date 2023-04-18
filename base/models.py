from django.db import models
from datetime import date
# Create your models here.


# class Category(models.Model):
#     # task = models.ForeignKey(Task, on_delete=models.CASCADE)


#     def __str__(self):
#         return self.name


# class Date(models.Model):
#     # task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     # date = models.DateField(default=date.today, null=True)

#     def __str__(self):
#         return str(self.date)


# class Desc(models.Model):
#     # task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     # desc = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return str(self.desc[0:20])


class Task(models.Model):
    name = models.CharField(max_length=200)
    # desc = models.ForeignKey(
    #     Desc, on_delete=models.SET_NULL, null=True)
    desc = models.TextField(null=True, blank=True)
    # date = models.ForeignKey(
    #     Date, on_delete=models.SET_NULL, null=True)
    date = models.DateField(default=date.today, null=True)
    category = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
