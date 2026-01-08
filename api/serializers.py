from rest_framework import serializers
from .models import DailyRecord

class DailyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyRecord
        fields = ['id', 'created_at', 'point', 'name', 'time']