from django_filters import rest_framework as filters
from .models import Numbers


class NumberRangeFilter(filters.FilterSet):
    min_number = filters.NumericRangeFilter(field_name="number", lookup_expr='gte')
    max_number = filters.NumericRangeFilter(field_name="number", lookup_expr='lte')

    class Meta:
        model = Numbers
        fields = ['min_number', 'max_number']