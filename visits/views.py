import imp
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import VisitsSerializer
from .models import Visits


class VisitsListCreateView(ListCreateAPIView):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer


class VisitsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer
    #  permission_classes
