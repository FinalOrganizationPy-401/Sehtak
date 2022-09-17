from asyncio import streams
from dataclasses import field
from account.models import Patient
from rest_framework import serializers
# from servicesmanager.models import Medicine, Tests,X_Rays
from django.contrib.auth import get_user_model

from .models import Visits
# from servicesmanager.models import PatientProfile

class VisitsSerializer(serializers.ModelSerializer):
    # patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    # patient = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.U )
    patient = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Visits
        # fields = ['patient','doctor','pharmacist','lab','x_rays_lab','medicine','test','x_rays']

        # def get_patient(self,obj):
            
  
        fields = '__all__'
        
   
