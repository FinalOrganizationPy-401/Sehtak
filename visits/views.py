# import imp
# from django.shortcuts import render
from account.models import PatientProfile
from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView

from .serializers import VisitsSerializer
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
        return serializer.save(patient=patient)


class PatientVisitsView(ListAPIView):
    '''
    Get all visits related for one user 
    '''
    def get_queryset(self):
        patient = PatientProfile.objects.get(user=self.request.user.id)
        data = Visits.objects.filter(patient=patient)
        print(data)
        return data

    serializer_class = VisitsSerializer



class VisitsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsPatientOrReadOnly]
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer
   
# user visits 
# doctor v 