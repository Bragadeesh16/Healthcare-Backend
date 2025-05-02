from rest_framework import serializers
from myapp.models import DoctorProfile, PatientProfile, PatientDoctorMapping
from account.models import CustomUser


class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        exclude = ["doctor_id"]


class PatientProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientProfile
        exclude = ["patient_id"]


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    doctor = DoctorProfileSerializer(read_only=True)
    patient = PatientProfileSerializer(read_only=True)
    doctor_id = serializers.UUIDField(write_only=True)
    patient_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ["id", "patient", "doctor", "patient_id", "doctor_id"]
