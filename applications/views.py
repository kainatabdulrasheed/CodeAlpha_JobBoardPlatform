from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Candidate, Resume, Application, Notification
from .serializers import ResumeSerializer, ApplicationSerializer, NotificationSerializer
from jobs.models import Job


@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_resume(request):
    candidate = get_object_or_404(Candidate, user=request.user)
    serializer = ResumeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(candidate=candidate)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def apply_to_job(request):
    candidate = get_object_or_404(Candidate, user=request.user)
    job = get_object_or_404(Job, pk=request.data.get('job'))
    resume = get_object_or_404(Resume, pk=request.data.get('resume'), candidate=candidate)

    if not job.is_active:
        return Response({'error': 'This job is no longer active'}, status=400)

    if Application.objects.filter(job=job, candidate=candidate).exists():
        return Response({'error': 'You already applied to this job'}, status=400)

    application = Application.objects.create(job=job, candidate=candidate, resume=resume)

    Notification.objects.create(
        employer=job.employer,
        message=f"{candidate.user.username} applied to your job '{job.title}'"
    )

    serializer = ApplicationSerializer(application)
    return Response(serializer.data, status=201)


@api_view(['GET'])
def my_applications(request):
    candidate = get_object_or_404(Candidate, user=request.user)
    applications = Application.objects.filter(candidate=candidate)
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def job_applications(request, job_id):
    job = get_object_or_404(Job, pk=job_id, employer__user=request.user)
    applications = Application.objects.filter(job=job)
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_status(request, pk):
    application = get_object_or_404(Application, pk=pk, job__employer__user=request.user)
    new_status = request.data.get('status')
    if new_status not in dict(Application.STATUS_CHOICES):
        return Response({'error': 'Invalid status'}, status=400)
    application.status = new_status
    application.save()
    serializer = ApplicationSerializer(application)
    return Response(serializer.data)


@api_view(['GET'])
def notifications(request):
    notes = Notification.objects.filter(employer__user=request.user)
    serializer = NotificationSerializer(notes, many=True)
    return Response(serializer.data)