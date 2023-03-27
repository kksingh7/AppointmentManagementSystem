from django.contrib import admin
from .models import Patient, Doctor, Appointment

# Register your models here.

model_list = [Patient, Doctor, Appointment]
admin.site.register(model_list)