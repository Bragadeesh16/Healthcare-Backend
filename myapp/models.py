from django.db import models
from account.models import CustomUser
import uuid

# Create your models here.

GENDER_CHOICES = (
    ('MALE','MALE'),
    ('FEMALE',"FEMALE"),
)

class DoctorProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    doctor_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    gender = models.CharField(max_length=10 ,choices= GENDER_CHOICES)
    date_of_birth = models.DateField()
    

    def __str__(self):
        return self.user.email
    
class PatientProfile(models.Model): 
    patient_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length = 15, choices = GENDER_CHOICES)


# class Patient_Doctor_Mapping(models.Model):
#     patient = models.ForeignKey(, on_delete=models.CASCADE, related_name="patient")
#     doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="doctor")
    

#     def __str__(self):
#         return f"{self.patient} - {self.doctor}"