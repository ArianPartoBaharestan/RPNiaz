from rest_framework import generics
from configurations.models import Configure
from .serializers import ConfigureSerializer
from core.error_manager import ErrorHandler


class ConfigurationView(generics.ListAPIView):
    serializer_class = ConfigureSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Configure.objects.all()
        if not queryset.exists():
            raise ErrorHandler.get_error_exception(404, 'general')
        return queryset
