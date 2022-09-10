from django.contrib import admin
from .models import PatientProfile,DoctorProfile, User, PharmacistProfile,X_rays_labProfile,LabsProfile

# Register your models here.
admin.site.register(User)
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(PharmacistProfile)
admin.site.register(X_rays_labProfile)
admin.site.register(LabsProfile)