from django.contrib import admin
from .models import Doctor, Specialization, Location, Patient
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(Location)
admin.site.register(Patient)