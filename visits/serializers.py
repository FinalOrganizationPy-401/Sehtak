from asyncio import streams
from dataclasses import field
from account.models import Patient
from rest_framework import serializers
from servicesmanager.models import Medicine, Tests,X_Rays
# from django.contrib.auth import get_user_model

from .models import Visits


class VisitsSerializer(serializers.ModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    # test = models.ForeignKey(Test, on_delete=models.CASCADE)

    # test = serializers.serialize(source='test.names')
    # medicine = serializers.SerializerMethodField('get_medicine')

    # test = serializers.Serializer("xml",Tests.objects[1])
    # x_rays = serializers.RelatedField(  )
    # print(test,'testtesttesttesttesttest')
    # medicine = serializers.CharField(source='medicine.names')

    # medicine = serializers.SerializerMethodField()
    # def get_medicine(self,obj):
    #     print(obj,'<<<<<<<<<<<<<<<<<')
    #     return obj.medicine.all()

    # doctor_id = serializers.SerializerMethodField()
    # def get_doctor_id(self,obj):
    #     data
    #     try:
    #         data = {
    #         'name':obj.doctor_id.name,
    #         'phone':str(obj.doctor_id.phone),
    #         'city' :obj.doctor_id.city,
    #         'location':obj.doctor_id.location
    #     }
    #     except:
            
    #     return data
    

    class Meta:
        model = Visits
        # fields = ['patient_id','doctor_id','pharmacist_id','lab_id','x_rays_lab_id','summary','description','prescription','medicine','test','x_rays']
        fields = '__all__'
        
   
