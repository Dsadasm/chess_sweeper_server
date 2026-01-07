from django_filters import rest_framework as filters
from api.models import DailyRecord

class DialyRecordFilter(filters.FilterSet):
    class Meta:
        model = DailyRecord
        fields = {
            'created_at': ['exact', 'lt', 'gt'],
            'points': ['exact', 'lt', 'gt'],
            'name': ['exact', 'icontains'],
        }