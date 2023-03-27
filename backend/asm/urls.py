from django.contrib import admin
from django.urls import path
from .views import PatientView, DoctorView, AppointmentView

urlpatterns = [
    path('patient/', PatientView.as_view()),
    path("patient/<int:pk>/", PatientView.as_view()),
    path("patient/<int:fk>/appointment/", AppointmentView.get_app_patient),
    path('doctor/', DoctorView.as_view()),
    path("doctor/<int:pk>/", DoctorView.as_view()),
    path("doctor/<int:fk>/appointment/", AppointmentView.get_app_doc),
    # path()
]

