from django.db import models

class Employee(models.Model):
    last_name = models.TextField(max_length=20, default='')
    first_name = models.TextField(max_length=20, default='')
    job_title = models.TextField(max_length=20, default='')
    job_description = models.TextField(max_length=50, default='')
    bio = models.TextField(max_length=255, default='')
    skills = models.TextField(max_length=255, default='')

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ('last_name',)
        unique_together = ('last_name', 'first_name')