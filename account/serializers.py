# from tkinter.ttk import Style
from dataclasses import fields
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from rest_framework.validators import UniqueValidator
from .models import Patient,PatientProfile, DoctorProfile,PharmacistProfile,LabsProfile,X_rays_labProfile, User as UserModel
# from django.contrib.auth import authenticate

User = Patient

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user): #2 
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        user_data =''
        # if user.role == "ADMIN":
        #     user_data = PatientProfile.objects.get(user=user.id)
        if user.role == "DOCTOR":
            user_data = DoctorProfile.objects.get(user=user.id)
        elif user.role == "PHARMACIST":
            user_data = PharmacistProfile.objects.get(user=user.id)
        elif user.role == "LABS":
            user_data = LabsProfile.objects.get(user=user.id)
        elif user.role == "X_RAYS_LAB":
            user_data = X_rays_labProfile.objects.get(user=user.id)
        elif user.role == "PATIENT":
            user_data = PatientProfile.objects.get(user=user.id)
        
        token['info_id'] = user_data.id
        token['username'] = user.username

        return token

# Register a new user
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,  
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True,style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ('email','password')
        extra_kwargs = {
           "password" : {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if instance is not None:
            instance.set_password(password)
        instance.save()
        return instance

class PatientProfileSerializer(serializers.ModelSerializer):
    '''
        Get patient details 
    '''
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    print(user, "user in serrrr")
    class Meta:
        model = PatientProfile
        fields = '__all__'
        extra_kwargs = {
           "password" : {'write_only': True}
        }

class DoctorSerializer(serializers.ModelSerializer):
    '''
    Get list of doctors
    '''
    class Meta:
        model = DoctorProfile
        fields = '__all__'

class DoctorProfileSerializer(serializers.ModelSerializer):
    '''
        Get doctor info 
    '''
    class Meta:
        model = DoctorProfile
        fields = '__all__'

class PharmacistSerializer(serializers.ModelSerializer):
     class Meta:
        model = PharmacistProfile
        fields = '__all__'

class PharmacistProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model = PharmacistProfile
        fields = '__all__'


class LabsSerializer(serializers.ModelSerializer):
     class Meta:
        model = LabsProfile
        fields = '__all__'

class LabProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model = LabsProfile
        fields = '__all__'

class X_raysSerializer(serializers.ModelSerializer):
     class Meta:
        model = X_rays_labProfile
        fields = '__all__'

class X_rayProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model = X_rays_labProfile
        fields = '__all__'

