from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Medicine, Tests, X_Ray


class MedicineListCreateView(ListCreateAPIView):
    queryset = Medicine.objects.all()
    #  serializer_class 
   

class MedicineRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Medicine.objects.all()
    #  serializer_class 
    #  permission_classes

class TestsListCreateView(ListCreateAPIView):
    queryset = Tests.objects.all()
    #  serializer_class 


class TestsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Tests.objects.all()
    #  serializer_class 
    #  permission_classes

class X_RaysListCreateView(ListCreateAPIView):
    queryset = X_Ray.objects.all()
    #  serializer_class 


class X_RaysRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = X_Ray.objects.all()
    #  serializer_class 
    #  permission_classes
