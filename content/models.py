from django.db import models


class Employee(models.Model):
    last_name = models.TextField(max_length=20, null=False, blank=False)
    first_name = models.TextField(max_length=20, null=False, blank=False)
    job_title = models.TextField(max_length=20, null=False, blank=False)
    job_description = models.TextField(max_length=1000, null=False, blank=False)
    bio = models.TextField(max_length=1000, null=False, blank=False)
    skills = models.TextField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        unique_together = ('last_name', 'first_name')
        ordering = ('last_name',)
