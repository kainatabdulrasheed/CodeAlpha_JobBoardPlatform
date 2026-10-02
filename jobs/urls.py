from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.job_list, name='job-list'),
    path('jobs/<int:pk>/', views.job_detail, name='job-detail'),
    path('jobs/create/', views.create_job, name='job-create'),
    path('jobs/<int:pk>/manage/', views.manage_job, name='job-manage'),
]