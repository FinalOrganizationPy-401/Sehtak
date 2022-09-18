# import imp
# from django.shortcuts import render
from account.models import DoctorProfile, LabsProfile, PatientProfile, PharmacistProfile, X_rays_labProfile
from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView

from .serializers import VisitsSerializer,VisitDetailsSerializer
from .models import Visits
# from utils.permission import IsOwner


class CreateVisitView(CreateAPIView):
    '''
    Create new visit 
    '''
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer
    
    def perform_create(self, serializer):
        patient = PatientProfile.objects.get(user=self.request.user.id)
        # print(self.request.user,"self.request.user.id")

        return serializer.save(patient=patient)


class UserVisitsView(ListAPIView):
    '''
    Get all visits related for any user 
    '''
    def get_queryset(self):
        if self.request.user.role == 'DOCTOR':
            doctor = DoctorProfile.objects.get(user=self.request.user.id)
            data = Visits.objects.filter(doctor=doctor)
            return data

        elif self.request.user.role == 'PATIENT':
            patient = PatientProfile.objects.get(user=self.request.user.id)
            data = Visits.objects.filter(patient=patient)
            return data

        elif self.request.user.role == 'LABS':
            lab = LabsProfile.objects.get(user=self.request.user.id)
            
            data = Visits.objects.filter(lab=lab)
            return data

        elif self.request.user.role == 'PHARMACIST':
            pharmacist = PharmacistProfile.objects.get(user=self.request.user.id)
            
            data = Visits.objects.filter(pharmacist=pharmacist)
            return data

        elif self.request.user.role == 'X_RAYS_LAB':
            x_rays_lab = X_rays_labProfile.objects.get(user=self.request.user.id)
           
            data = Visits.objects.filter(x_rays_lab=x_rays_lab)
            return data

    serializer_class = VisitsSerializer



class VisitsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsPatientOrReadOnly]
    queryset = Visits.objects.all()
    serializer_class = VisitDetailsSerializer
   
# user visits 
# doctor v 