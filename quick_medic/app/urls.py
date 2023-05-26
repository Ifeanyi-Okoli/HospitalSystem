from django.urls import path
from .views import (
    Home,
    CreateDoctor,
    CreateSpecialization,
    SpecializationDetail,
    SpecializationList,
    RemoveSpecialization,
    UpdateSpecialization,
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('doctor', CreateDoctor.as_view(), name='create_doctor'),
    path('specialization', CreateSpecialization.as_view(), name='create_specialization'),
    path('specialization/<pk>', CreateSpecialization.as_view(), name='specialization_detail'),
    path('specialization/<pk>/update', UpdateSpecialization.as_view(), name='specialization_list'),
    path('specialization/<pk>/remove', RemoveSpecialization.as_view(), name='specialization_list'),
    path('specialization/all', SpecializationList.as_view(), name='specialization_list'),
    path('specialization/all', SpecializationDetail.as_view(), name='specialization_list'),
]