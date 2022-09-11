from django.contrib import admin
from .models import Tests, Medicine, X_Rays

# Register your models here.

admin.site.register(Tests)
admin.site.register(Medicine)
admin.site.register(X_Rays)
