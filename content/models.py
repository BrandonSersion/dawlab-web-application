from django.db import models

class Employee(models.Model):
    last_name = models.TextField(default='')
    first_name = models.TextField(default='')
    job_title = models.TextField(default='')
    job_description = models.TextField(default='')
    bio = models.TextField(default='')
    skills = models.TextField(default='')

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        unique_together = ('last_name', 'first_name')