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
    doctor_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False,null=True, blank=True)
    gender = models.CharField(max_length=10 ,choices= GENDER_CHOICES)
    date_of_birth = models.DateField()
    

    def __str__(self):
        return self.email
    
class PatientProfile(models.Model): 
    patient_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False,null=True, blank=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length = 15, choices = GENDER_CHOICES)


class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name="mappings")
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name="mappings")

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
