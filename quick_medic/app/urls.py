from django.urls import path, include
from .views import (
    Home,
    CreateDoctor, UpdateDoctor, RemoveDoctor, DoctorList, DoctorDetail,
    CreateSpecialization, SpecializationDetail, SpecializationList, RemoveSpecialization, UpdateSpecialization,
    CreateRequest, RequestDetail, RequestList, RemoveRequest, UpdateRequest,
    CreateAppointment, AppointmentDetail, AppointmentList, RemoveAppointment, UpdateAppointment,
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    #DOCTORS URLS
    path('doctor/', include(
        [
             path('create', CreateDoctor.as_view(), name='doctor_create'),
             path('<pk>', DoctorDetail.as_view(), name='doctor_detail'),
             path('list', DoctorList.as_view(), name='doctor_list'),
             path('<pk>/remove', RemoveDoctor.as_view(), name='doctor_remove'),
             path('<pk>/update', UpdateDoctor.as_view(), name='doctor_update'),
])),
    
    
    #REQUESTCONSULTANCY URLS
    path('request/', include(
        [
             path('create', CreateRequest.as_view(), name='request_create'),
             path('<pk>', RequestDetail.as_view(), name='request_detail'),
             path('list', RequestList.as_view(), name='request_list'),
             path('<pk>/remove', RemoveRequest.as_view(), name='request_remove'),
             path('<pk>/update', UpdateRequest.as_view(), name='request_update'),
])),



   #RAPPOINTMENT URLS
    path('appointment/', include(
        [
             path('create', CreateAppointment.as_view(), name='appointment_create'),
             path('<pk>', AppointmentDetail.as_view(), name='appointment_detail'),
             path('list', AppointmentList.as_view(), name='appointment_list'),
             path('<pk>/remove', RemoveAppointment.as_view(), name='appointment_remove'),
             path('<pk>/update', UpdateAppointment.as_view(), name='appointment_update'),
])),
    



    #SPECIALIZATION URLS
    path('specialization/', include(
        [
             path('create', CreateSpecialization.as_view(), name='create_specialization'),
             path('<pk>', SpecializationDetail.as_view(), name='specialization_detail'),
             path('<pk>/update', UpdateSpecialization.as_view(), name='specialization_update'),
             path('<pk>/remove', RemoveSpecialization.as_view(), name='specialization_remove'),
             path('', SpecializationList.as_view(), name='specialization_list'),
            #  path('all', SpecializationDetail.as_view(), name='specialization_detail'),
])),
]