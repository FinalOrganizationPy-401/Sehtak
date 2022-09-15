from asyncio import streams
from dataclasses import field
from account.models import Patient
from rest_framework import serializers
from servicesmanager.models import Medicine, Tests,X_Rays
# from django.contrib.auth import get_user_model

from .models import Visits


class VisitsSerializer(serializers.ModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
#       patient_id = serializers.PrimaryKeyRelatedField(queryset = get_user_model().objects.all(), source = "member", write_only=True)
    #  read_only_fields = ('userId',)

    class Meta:
        model = Visits
        # fields = ['patient_id','doctor_id','pharmacist_id','lab_id','x_rays_lab_id','summary','description','prescription','medicine','test','x_rays']
        fields = '__all__'
        
   
