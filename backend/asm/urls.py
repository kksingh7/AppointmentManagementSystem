from django.contrib import admin
from django.urls import path
from .views import PatientView, DoctorView, AppointmentViewDoctor, AppointmentViewPatient, AppointmentView

urlpatterns = [
    path('patient/', PatientView.as_view()),
    path("patient/<int:pk>/", PatientView.as_view()),
    path("patient/<int:fk>/appointment/", AppointmentViewPatient.as_view()),
    path('doctor/', DoctorView.as_view()),
    path("doctor/<int:pk>/", DoctorView.as_view()),
    path("doctor/<int:fk>/appointment/", AppointmentViewDoctor.as_view()),
    path('appointment/', AppointmentView.as_view())
    # path()
]

