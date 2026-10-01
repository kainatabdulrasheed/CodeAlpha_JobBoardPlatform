from django.contrib import admin
from .models import Employer, Job

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'location', 'is_active')
    list_filter = ('is_active', 'job_type')
    search_fields = ('title', 'location')
