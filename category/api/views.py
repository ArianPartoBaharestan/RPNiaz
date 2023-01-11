from rest_framework import generics
from category.models import Category, Brand
from .serializers import CategorySerializer, BrandSerializer
from core.error_manager import ErrorHandler


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Category.objects.all()
        if not queryset.exists():
            raise ErrorHandler.get_error_exception(404, 'general')
        return queryset


class BrandView(generics.ListAPIView):
    serializer_class = BrandSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Brand.objects.all()
        if not queryset.exists():
            raise ErrorHandler.get_error_exception(404, 'general')
        return queryset
