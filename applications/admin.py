from django.contrib import admin
from .models import Candidate, Resume, Application, Notification

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'phone')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'uploaded_at')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job', 'status', 'applied_at')
    list_filter = ('status',)
    search_fields = ('candidate__user__username', 'job__title')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('employer', 'message', 'is_read', 'created_at')
    list_filter = ('is_read',)
