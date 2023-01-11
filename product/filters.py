from django_filters.rest_framework import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'Category_id': ['exact'],
            'price': ['lt', 'gt'],
            'product_status':['exact']
        }

