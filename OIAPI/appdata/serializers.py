from rest_framework import serializers
from .models import Appdata,Refined

class AppdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appdata
        fields = '__all__'

class RefinedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refined
        fields = '__all__'