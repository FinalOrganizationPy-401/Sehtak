from tkinter.ttk import Style
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

# from account.models import User
User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)


        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(min_length=8, write_only=True,style={'input_type': 'password'})
    
# ,'first_name','last_name','phone','birth_date','gender','height','weight','blood_type','allergies'
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