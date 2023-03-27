from django.db import models

# Create your models here.


class Patient(models.Model):
    patientId = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=250, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.PositiveIntegerField(blank=False, null=False)


class Doctor(models.Model):
    doctorId = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.PositiveIntegerField()


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
