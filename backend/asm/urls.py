from django.contrib import admin
from django.urls import path
from .views import PatientView, DoctorView

urlpatterns = [
    path('patient/', PatientView.as_view()),
    path("patient/<int:pk>/", PatientView.as_view()),
    path('doctor/', DoctorView.as_view()),
    path("doctor/<int:pk>/", DoctorView.as_view()),
]