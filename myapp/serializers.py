from rest_framework import serializers
from myapp.models import DoctorProfile, PatientProfile
from account.models import CustomUser

class DoctorProfileSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(required = True)
    class Meta:
        model = DoctorProfile
        exclude = ['doctor_id']
    

class PatientProfileSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(required = True)
    class Meta:
        model = PatientProfile
        exclude = ["patient_id"]
