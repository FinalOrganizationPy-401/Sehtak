from .serializers import MyTokenObtainPairSerializer, RegisterSerializer,PatientProfileSerializer,DoctorSerializer,DoctorProfileSerializer,PharmacistSerializer, PharmacistProfileSerializer,LabsSerializer,LabProfileSerializer,X_raysSerializer,X_rayProfileSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth import get_user_model


from utils.permission import IsOwner,IsOwnerOrReadOnly
from .models import PatientProfile as PatientProfileModel, DoctorProfile,PharmacistProfile,LabsProfile,X_rays_labProfile

# Login View 
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

# Register View 
class RegisterView(generics.CreateAPIView):
    User = get_user_model()

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# Patient Profile view 
class PatientProfileView(generics.RetrieveUpdateDestroyAPIView):
    '''
     patient profile View : allowed get, update, delet  
    '''
    User = PatientProfileModel
    queryset = User.objects.all()
    serializer_class = PatientProfileSerializer
    # permission_classes = [IsOwner]


class DoctorView(generics.ListAPIView):
    '''
    view list of doctor Profiles
    '''
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorSerializer

class DoctorProfileView(generics.RetrieveUpdateDestroyAPIView):
    '''
    view doctor Profile details with ability to edit and update information
    '''
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

class PharmacistView(generics.ListAPIView):
    '''
    view list of Pharmacist Profiles
    '''
    queryset = PharmacistProfile.objects.all()
    serializer_class = PharmacistSerializer

class PharmacistProfileView(generics.RetrieveUpdateDestroyAPIView):
    '''
    view Pharmacist Profile details with ability to edit and update information
    '''
    queryset = PharmacistProfile.objects.all()
    serializer_class = PharmacistProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]


class LabsView(generics.ListAPIView):
    '''
    view list of Lab Profiles
    '''
    queryset = LabsProfile.objects.all()
    serializer_class = LabsSerializer

class LabProfileView(generics.RetrieveUpdateDestroyAPIView):
    '''
    view Labs Profile details with ability to edit and update information
    '''
    queryset = LabsProfile.objects.all()
    serializer_class = LabProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

class X_raysView(generics.ListAPIView):
    '''
    view list of Lab Profiles
    '''
    queryset = X_rays_labProfile.objects.all()
    serializer_class = X_raysSerializer

class X_raysProfileView(generics.RetrieveUpdateDestroyAPIView):
    '''
    view Labs Profile details with ability to edit and update information
    '''
    queryset = X_rays_labProfile.objects.all()
    serializer_class = X_rayProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]