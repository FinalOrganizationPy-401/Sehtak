from .serializers import MyTokenObtainPairSerializer, RegisterSerializer,PatientProfileSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth import get_user_model

from utils.permission import IsOwner
from .models import PatientProfile as PatientProfileModel

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    User = get_user_model()

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class PatientProfileView(generics.RetrieveUpdateDestroyAPIView):
    '''
     patient profile View : allowed get, update, delet  
    '''
    User = PatientProfileModel
    queryset = User.objects.all()
    serializer_class = PatientProfileSerializer
    permission_classes = [IsOwner]

