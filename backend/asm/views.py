from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import PatientSerializer, DoctorSerializer, AppointmentSerializer
from django.http.response import JsonResponse
from rest_framework.response import Response
from .models import Patient, Doctor, Appointment


# Create your views here.

class PatientView(APIView):

    def post(self, request):
        data = request.data
        serializer = PatientSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(200)
        return Response(serializer.errors)

    def get_patient(self, pk):
        try:
            patient = Patient.objects.get(patientId=pk)
            serializer = PatientSerializer(patient, many=False)
            return Response(serializer.data)
        except Patient.DoesNotExist():
            return Response(404)

    def get(self, request, pk=None):
        if pk:
            data = self.get_patient(pk)
            return data
        else:
            data = Patient.objects.all()
            serializer = PatientSerializer(data, many=True)
            return Response(serializer.data)

    def delete(self, request, pk=None):
        patient = Patient.objects.get(patientId=pk)
        patient.delete()
        return Response(200)

class AppointmentViewDoctor(APIView):
    def get(self, request, fk=None):
        data = Appointment.objects.filter(doctor_id=fk)
        serializer = AppointmentSerializer(data, many=True)
        return Response(serializer.data)


class AppointmentViewPatient(APIView):

    def get(self, request, fk=None):
        data = Appointment.objects.filter(patient_id=fk)
        serializer = AppointmentSerializer(data, many=True)
        return Response(serializer.data)


class AppointmentView(APIView):

    def post(self, request):
        data = request.data
        serializer = AppointmentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(200)
        return Response(serializer.errors)


    def delete(self, request, pk=None):
        appointment = Appointment.get(id=pk)
        appointment.delete()
        return Response(200)


class DoctorView(APIView):

    def post(self, request):
        data = request.data
        serializer = DoctorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(200)
        return Response(serializer.errors)

    def get_doctor(self, pk):
        try:
            doctor = Doctor.objects.get(doctorId=pk)
            serializer = DoctorSerializer(doctor, many=False)
            return Response(serializer.data)
        except Patient.DoesNotExist():
            return Response(404)

    def get(self, request, pk=None):
        if pk:
            data = self.get_doctor(pk)
            return data
        else:
            data = Doctor.objects.all()
            serializer = DoctorSerializer(data, many=True)
            return Response(serializer.data)

    def delete(self, request, pk=None):
        doctor = Doctor.objects.get(doctorId=pk)
        doctor.delete()
        return Response(200)