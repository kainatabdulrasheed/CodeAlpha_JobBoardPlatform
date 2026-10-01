from django.db import models
from django.contrib.auth.models import User

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=400)
    description = models.TextField(blank=True)

class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=300)
    location = models.CharField(max_length=500)
    JOB_TYPE_CHOICES = [
    ('full_time', 'Full Time'),
    ('part_time', 'Part Time'),
    ('internship', 'Internship'),
    ('contract', 'Contract'),
]
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default= True)