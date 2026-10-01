from rest_framework import serializers
from .models import Employer, Job

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    employer = serializers.ReadOnlyField(source='employer.company_name')

    class Meta:
        model = Job
        fields = '__all__'