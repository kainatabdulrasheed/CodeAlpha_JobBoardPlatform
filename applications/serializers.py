from rest_framework import serializers
from .models import Candidate, Resume, Application, Notification
from jobs.serializers import JobSerializer

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    candidate = serializers.ReadOnlyField(source='candidate.id')

    class Meta:
        model = Resume
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    candidate = serializers.ReadOnlyField(source='candidate.id')
    status = serializers.ReadOnlyField()

    class Meta:
        model = Application
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['job'] = JobSerializer(instance.job).data
        return rep

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'