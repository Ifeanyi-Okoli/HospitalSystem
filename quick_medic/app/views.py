from django.shortcuts import render
from django.views import View #using this view requires defining a generic method - get or post
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

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
    
    
class CreateUser(CreateView):
    def post(self, request):
        content_type = ContentType.objects.get_for_model(RequestConsultation)
        user = User(username ='user1', first_name='Maruf', last_name='Ogundele', password='password',)
        user_permission = Permission.objects.filter(content_type = content_type)
        user.user_permissions.add(user_permission)
        user.save()
        
    
    #DOCTOR MODELS
class CreateDoctor(CreateView):
    model = Doctor
    # template_name = 'app/create_doctor.html'
    fields = '__all__'
    exclude = ('is_verified', 'is_booked')
    success_url = '/'
    
    # def post(self, request):
    #     if request.method == 'POST' and request.FileUpload():
    #         pass


class DoctorDetail(PermissionRequiredMixin, DetailView):
    model = Doctor
    permission_required = ('app.can_view_doctor_detail')
class DoctorList(ListView):
    model = Doctor
    
class RemoveDoctor(LoginRequiredMixin, DeleteView):
    model = Doctor
    permission_required = ('app.can_view_doctor_detail')
    login_url = '/'
    
class UpdateDoctor(UpdateView):
    model = Doctor
    fields= '__all__'




#SPECIALIZATION MODELS

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
    login_url = '/'
    
class UpdateSpecialization(UpdateView):
    model = Specialization
    fields= '__all__'
    
    
    #APPOINTMENT MODELS
    
        
class CreateAppointment(CreateView):
    model = Appointment
    template_name = 'app/doctor_form.html'
    fields = '__all__'
    exclude = ('is_verified', 'is_booked')
    success_url = '/'


class AppointmentDetail(PermissionRequiredMixin, DetailView):
    model = Appointment

class AppointmentList(ListView):
    model = Appointment
    
class RemoveAppointment(LoginRequiredMixin, DeleteView):
    model = Appointment
    login_url = '/'
    
class UpdateAppointment(UpdateView):
    model = Appointment
    fields= '__all__'
    
    
    #REQUESTCONSULTANCY MODELS
    
class CreateRequest(CreateView):
    model = RequestConsultation
    template_name = 'app/doctor_form.html'
    fields = '__all__'
    success_url = "/"
    

class RequestDetail(PermissionRequiredMixin, DetailView):
    model = RequestConsultation
    
class RequestList(ListView):
    model = RequestConsultation
    
class RemoveRequest(LoginRequiredMixin, DeleteView):
    model = RequestConsultation
    login_url = '/'
    
class UpdateRequest(UpdateView):
    model = RequestConsultation
    fields= '__all__'
    
    #SYMPTOMS MODELS
    