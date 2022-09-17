# from tkinter.ttk import Style
from dataclasses import fields
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from rest_framework.validators import UniqueValidator
from .models import Patient,PatientProfile, DoctorProfile,PharmacistProfile,LabsProfile,X_rays_labProfile
from django.template import RequestContext

# from account.models import User
User = Patient
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # print(cls,"cls>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # print(token,"token>>>>>>>>>>>>>>>>>>>>>>>>>>")

        token['username'] = user.username
        # get_user(token)
        return token


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

