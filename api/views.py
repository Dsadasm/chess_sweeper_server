from rest_framework import viewsets
from .models import DailyRecord
from .serializers import DailyRecordSerializer
from .filters import DialyRecordFilter
from django_filters import rest_framework as filters
from rest_framework.permissions import AllowAny


class DialyRecordViewSet(viewsets.ModelViewSet):
    queryset = DailyRecord.objects.all()
    serializer_class = DailyRecordSerializer
    filterset_class = DialyRecordFilter
    filter_backends = (filters.DjangoFilterBackend,)
    permission_classes = [AllowAny]