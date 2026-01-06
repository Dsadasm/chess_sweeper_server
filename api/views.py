from rest_framework import viewsets
from .models import DailyRecord
from .serializers import DailyRecordSerializer


class DialyRecordViewSet(viewsets.ModelViewSet):
    queryset = DailyRecord.objects.all().order_by('-date')
    serializer_class = DailyRecordSerializer