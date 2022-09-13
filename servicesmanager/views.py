from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Medicine, Tests, X_Rays
from .serializers import X_RaysSerializer, TestsSerializer, MedicineSerializer
from .permissions import IsOwnerOrReadOnly

class MedicineListCreateView(ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class MedicineRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsOwnerOrReadOnly]


class TestsListCreateView(ListCreateAPIView):
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer


class TestsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer
    #  permission_classes


class X_RaysListCreateView(ListCreateAPIView):
    queryset = X_Rays.objects.all()
    serializer_class = X_RaysSerializer


class X_RaysRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = X_Rays.objects.all()
    serializer_class = X_RaysSerializer
    #  permission_classes
