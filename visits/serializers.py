from rest_framework import serializers

from account.serializers import DoctorProfileSerializer, LabsSerializer, PharmacistProfileSerializer, X_rayProfileSerializer,LabProfileSerializer
from .models import Visits
from account.models import DoctorProfile

class VisitsSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Visits
        fields = '__all__'
        

class VisitDetailsSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)
    doctor = DoctorProfileSerializer()
    lab = LabProfileSerializer()
    pharmacist = PharmacistProfileSerializer()
    x_rays_lab = X_rayProfileSerializer()
    
    # lab = LabsSerializer()
    class Meta:
        model = Visits
        fields = '__all__'
        
