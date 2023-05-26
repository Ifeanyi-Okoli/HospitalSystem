from django.shortcuts import render
from django.views import View #using this view requires defining a generic method - get or post
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import mixin

from .models import (
    Doctor,
    RequestConsultation,
    Appointment,
    Symptoms,
    Drugs,
    MedicalHistory,
    Specialization,
)
# Create your views here.

class Home(View):
    def get(self, request):
        # return render(request, 'app/home.html')
        return HttpResponse("<h1>This is my Quick Medic Home Page</h1>"
                            '<p>It is a simple app that helps you get medical consultation from the comfort of your home</p>'
                            )
    
    def post(self, request):
        pass
    
class CreateDoctor(CreateView):
    model = Doctor
    # template_name = 'app/create_doctor.html'
    fields = '__all__'
    exclude = ('is_verified', 'is_booked')
    success_url = '/'
    

class CreateSpecialization(CreateView):
    model = Specialization
    # template_name = 'app/create_doctor.html'
    fields = '__all__'
    success_url = "/"
    

class SpecializationDetail(DetailView):
    model = Specialization

class SpecializationList(ListView):
    model = Specialization
    
class RemoveSpecialization(DeleteView):
    model = Specialization
    
class UpdateSpecialization(UpdateView):
    model = Specialization