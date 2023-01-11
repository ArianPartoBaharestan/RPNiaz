from .serializers import ProvinceSerializer, CitySerializer
from city.models import Province, City
from rest_framework import generics
from core.error_manager import ErrorHandler


class ProvinceView(generics.ListAPIView):
    serializer_class = ProvinceSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Province.objects.prefetch_related('cities').all()

        if not queryset.exists():
            raise ErrorHandler.get_error_exception(404, 'general')
        return queryset


class CityView(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self, *args, **kwargs):
        queryset = City.objects.all()
        if not queryset.exists():
            raise ErrorHandler.get_error_exception(404, 'general')
        return queryset
