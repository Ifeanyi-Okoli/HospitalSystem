from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse
# from django.contrib.gis import models

# Create your models here.
STATUS = (('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined'))

class Location(models.Model):
    pass
#     name = models.CharField(max_length=100)
#     country = models.CharField(max_length=200)
#     city = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.name

# class Specialization(models.Model):
#     name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name


class Specialization(models.Model):
    name = models.CharField(max_length=200)
    
    # def get_absolute_url(self):
        # return reverse("specialization_detail", kwargs={"pk": self.pk})
        
    def __str__(self):
        return self.name

class Doctor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    is_booked = models.BooleanField(default=False)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    speciality = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    portfolio_number = models.CharField(max_length=200)
    # hospital = models.CharField(max_length=100)
    # address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='pics')
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.name
    

class Patient(models.Model):
    pass
    # name = models.CharField(max_length=100)
    # age = models.CharField(max_length=100)
    # address = models.CharField(max_length=100)
    # phone = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='pics')
    # def __str__(self):
    #     return self.name

class RequestConsultation(models.Model):
    """Request consultation with available doctor. The doctor sets a]ointment if consultation is accepted
    """
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests")
    doctor = models.ForeignKey(Doctor, related_name='consultations', on_delete=models.SET_NULL, null= True, verbose_name='Request for consultataion')
    symptoms = models.TextField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS)
    
    def __str__(self) -> str:
        return f"{self.patient} - {self.status}"

class Appointment(models.Model):
    consult = models.ForeignKey(RequestConsultation, verbose_name='Consultation', on_delete=models.CASCADE, max_length=100)
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    # patient = models.OneToOneField(User, on_delete=models.CASCADE, related_name="my_appointments")
    date = models.DateTimeField(verbose_name="Appointment Date and Time")
    # reason = models.TextField(verbose_name="Reason for Appointment")
    type = models.CharField(max_length=100, choices=(('virtual', 'Virtual'), ('physical', 'Physical'), ('private', 'private')))
    # time = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.type} - {self.consult.doctor} - {self.date}"
    

class Symptoms(models.Model):
    name = models.CharField(max_length=200, verbose_name="Symptom Name")
    
    def __str__(self) -> str:
        return self.name

class Drugs(models.Model):
    name = models.CharField(max_length=200, verbose_name="Drug Name")
    description = models.TextField(verbose_name="Description of Drug")
    
    def __str__(self) -> str:
        return self.name

class MedicalHistory(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="medical_history", max_length=100)
    illness = models.CharField(max_length=200, verbose_name="Illness Name")
    symptoms = models.ManyToManyField(Symptoms, related_name="medical_history")
    drugs = models.ManyToManyField('Drugs', related_name="medical_history")
    alergies = models.TextField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Patients Attended")
    date = models.DateTimeField(verbose_name="Date of Medical History")
    # description = models.TextField(verbose_name="Description of Medical History")
    
    def __str__(self) -> str:
        return f"{self.drugs} - {self.illness} - {self.date} - {self.doctor}"