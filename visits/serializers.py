from rest_framework import serializers
# from django.contrib.auth import get_user_model

from .models import Visits

class VisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        fields = '__all__'


# https://stackoverflow.com/questions/66761924/django-rest-framework-get-data-from-related-table