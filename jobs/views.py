from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Job, Employer
from .serializers import JobSerializer

@api_view(['GET'])
def job_list(request):
    jobs = Job.objects.filter(is_active=True)

    location = request.query_params.get('location')
    job_type = request.query_params.get('job_type')
    keyword = request.query_params.get('keyword')

    if location:
        jobs = jobs.filter(location__icontains=location)
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    if keyword:
        jobs = jobs.filter(title__icontains=keyword)

    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    serializer = JobSerializer(job)
    return Response(serializer.data)


@api_view(['POST'])
def create_job(request):
    employer = get_object_or_404(Employer, user=request.user)
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(employer=employer)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PATCH', 'DELETE'])
def manage_job(request, pk):
    job = get_object_or_404(Job, pk=pk, employer__user=request.user)

    if request.method == 'DELETE':
        job.delete()
        return Response(status=204)

    serializer = JobSerializer(job, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)