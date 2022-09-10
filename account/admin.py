from django.contrib import admin
from .models import PatientProfile,DoctorProfile, User

# Register your models here.
admin.site.register(User)
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)