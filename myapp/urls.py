from django.urls import path
from myapp.views import (
    DoctorListCreateView, DoctorRetrieveUpdateDeleteView,
    PatientListCreateView, PatientRetrieveUpdateDeleteView,
    AssignDoctorView, AllMappingsView, DoctorsByPatientView, DeleteMappingView
)

urlpatterns = [
    path('doctors/', DoctorListCreateView.as_view(), name='doctor_list_create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDeleteView.as_view(), name='doctor_detail'),

    path('patients/', PatientListCreateView.as_view(), name='patient_list_create'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDeleteView.as_view(), name='patient_detail'),

    path('api/mappings/', AssignDoctorView.as_view(), name='assign-doctor'),
    path('api/mappings/', AllMappingsView.as_view(), name='all-mappings'),
    path('api/mappings/<uuid:patient_id>/', DoctorsByPatientView.as_view(), name='doctors-by-patient'),
    path('api/mappings/<int:id>/', DeleteMappingView.as_view(), name='delete-mapping'),
]
