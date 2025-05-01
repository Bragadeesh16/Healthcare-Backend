from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.models import DoctorProfile, PatientProfile
from myapp.serializers import DoctorProfileSerializer, PatientProfileSerializer


class DoctorListCreateView(APIView):
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
