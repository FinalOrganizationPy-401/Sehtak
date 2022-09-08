from django.contrib import admin
from .models import Tests,Medicines, X_Rays

# Register your models here.

admin.site.register(Tests,Medicines, X_Rays)