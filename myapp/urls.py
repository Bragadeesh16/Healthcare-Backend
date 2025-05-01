from django.urls import path
from myapp.views import (
    DoctorListCreateView, DoctorRetrieveUpdateDeleteView,
    PatientListCreateView, PatientRetrieveUpdateDeleteView
)

urlpatterns = [
    path('doctors/', DoctorListCreateView.as_view(), name='doctor_list_create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDeleteView.as_view(), name='doctor_detail'),

    path('patients/', PatientListCreateView.as_view(), name='patient_list_create'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDeleteView.as_view(), name='patient_detail'),
]
