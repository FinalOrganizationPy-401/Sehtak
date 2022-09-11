from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import (
    PatientProfile,
    DoctorProfile,
    User,
    PharmacistProfile,
    X_rays_labProfile,
    LabsProfile,
)
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'role','is_staff', 'is_active',)
    list_filter = ('email','role', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('role','is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','role', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','role')
    ordering = ('email','role')



# Register your models here.
admin.site.register(User,CustomUserAdmin)
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(PharmacistProfile)
admin.site.register(X_rays_labProfile)
admin.site.register(LabsProfile)
