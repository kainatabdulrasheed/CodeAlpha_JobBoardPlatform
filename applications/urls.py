from django.urls import path
from . import views

urlpatterns = [
    path('resumes/', views.upload_resume, name='resume-upload'),
    path('applications/', views.apply_to_job, name='application-apply'),
    path('applications/my/', views.my_applications, name='application-my'),
    path('jobs/<int:job_id>/applications/', views.job_applications, name='job-applications'),
    path('applications/<int:pk>/status/', views.update_status, name='application-status'),
    path('notifications/', views.notifications, name='notification-list'),
]