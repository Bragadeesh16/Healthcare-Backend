from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.models import DoctorProfile, PatientProfile,PatientDoctorMapping
from myapp.serializers import (DoctorProfileSerializer, PatientProfileSerializer
                               ,PatientDoctorMappingSerializer)
from rest_framework.permissions import IsAuthenticated

class DoctorListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        doctors = DoctorProfile.objects.all()
        serializer = DoctorProfileSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoctorProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            doctor = DoctorProfile.objects.get(pk=pk)
            serializer = DoctorProfileSerializer(doctor)
            return Response(serializer.data)
        except DoctorProfile.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            doctor = DoctorProfile.objects.get(pk=pk)
            serializer = DoctorProfileSerializer(doctor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DoctorProfile.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            doctor = DoctorProfile.objects.get(pk=pk)
            doctor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DoctorProfile.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)


class PatientListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        patients = PatientProfile.objects.all()
        serializer = PatientProfileSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            patient = PatientProfile.objects.get(pk=pk)
            serializer = PatientProfileSerializer(patient)
            return Response(serializer.data)
        except PatientProfile.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            patient = PatientProfile.objects.get(pk=pk)
            serializer = PatientProfileSerializer(patient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PatientProfile.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            patient = PatientProfile.objects.get(pk=pk)
            patient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PatientProfile.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)


class AssignDoctorView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        patient_id = request.data.get('patient_id')
        doctor_id = request.data.get('doctor_id')

        try:
            patient = PatientProfile.objects.get(patient_id=patient_id)
            doctor = DoctorProfile.objects.get(doctor_id=doctor_id)
        except (PatientProfile.DoesNotExist, DoctorProfile.DoesNotExist):
            return Response({'error': 'Invalid patient_id or doctor_id'}, status=status.HTTP_400_BAD_REQUEST)

        mapping, created = PatientDoctorMapping.objects.get_or_create(patient=patient, doctor=doctor)
        serializer = PatientDoctorMappingSerializer(mapping)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

# GET /api/mappings/ - Retrieve all patient-doctor mappings
class AllMappingsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        mappings = PatientDoctorMapping.objects.all()
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# GET /api/mappings/<patient_id>/ - Get all doctors assigned to a specific patient
class DoctorsByPatientView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, patient_id):
        mappings = PatientDoctorMapping.objects.filter(patient__patient_id=patient_id)
        if not mappings.exists():
            return Response({'message': 'No mappings found for this patient'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# DELETE /api/mappings/<int:id>/ - Remove a doctor from a patient
class DeleteMappingView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        try:
            mapping = PatientDoctorMapping.objects.get(id=id)
            mapping.delete()
            return Response({'message': 'Mapping deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except PatientDoctorMapping.DoesNotExist:
            return Response({'error': 'Mapping not found'}, status=status.HTTP_404_NOT_FOUND)