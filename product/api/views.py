from product.models import Product
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, \
    DestroyAPIView
from .serializers import ListProductSerializer, CreateProductSerializer, DetailProductSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView, Response
from rest_framework import status
from django.http import Http404, HttpResponseNotFound
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from core.error_manager import ErrorHandler


# Product Views
class ListActiveProductsView(ListAPIView):
    serializer_class = ListProductSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'Brand', 'Category']
    filterset_class = ProductFilter

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.filter(status='True')
        if not queryset.exists():
            raise ErrorHandler.get_error_exception(404, 'general')
        return queryset


class ListAllProductsView(ListAPIView):
    serializer_class = ListProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.all()
        if not queryset.exists():
            raise ErrorHandler.get_error_exception(404, 'general')
        return queryset


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes = (IsAuthenticated,)


class DetailProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = DetailProductSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class ListUserActiveProducts(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = Product.objects.filter(seller=request.user, status=True)
        serilizer = ListProductSerializer(queryset, many=True)
        if not queryset.exists():
            raise ErrorHandler.get_error_exception(404, 'general')
        return Response(data=serilizer.data, status=status.HTTP_200_OK)


class ListUserWaitingProducts(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = Product.objects.filter(seller=request.user, status=False)
        serilizer = ListProductSerializer(queryset, many=True)
        if not queryset.exists():
            raise ErrorHandler.get_error_exception(404, 'general')
        return Response(data=serilizer.data, status=status.HTTP_200_OK)
