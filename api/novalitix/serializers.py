from rest_framework import serializers
from .models import PredictionData

class PredictionDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PredictionData
        fields = '__all__'