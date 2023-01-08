from rest_framework import generics
from category.models import Category
from .serializers import ConfigureSerializer


class ConfigurationView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ConfigureSerializer
