from rest_framework import serializers

# from django.contrib.auth import get_user_model

from .models import Medicine, Tests, X_Rays


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"


class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tests
        fields = "__all__"


class X_RaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = X_Rays
        fields = "__all__"
