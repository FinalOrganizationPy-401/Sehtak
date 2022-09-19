from rest_framework import serializers

from account.serializers import DoctorProfileSerializer
from .models import Visits
from account.models import DoctorProfile

class VisitsSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)
    doctor = DoctorProfileSerializer()
    class Meta:
        model = Visits
        fields = '__all__'

class CreateVisitsSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)
    # doctor = DoctorProfileSerializer()
    class Meta:
        model = Visits
        fields = '__all__'    

class VisitDetailsSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)
    doctor = DoctorProfileSerializer(read_only=True)
    # lab = LabProfileSerializer()
    # pharmacist = PharmacistProfileSerializer()
    # x_rays_lab = X_rayProfileSerializer()
    
    # lab = LabsSerializer()
    class Meta:
        model = Visits
        fields = '__all__'
        
