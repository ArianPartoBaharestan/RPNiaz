from .serializers import ProvinceSerializer, CitySerializer
from .models import Province, City
from rest_framework.generics import ListCreateAPIView


class ProvinceView(ListCreateAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class CityView(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
