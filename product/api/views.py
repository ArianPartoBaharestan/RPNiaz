from product.models import Product 
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveUpdateDestroyAPIView , ListCreateAPIView , DestroyAPIView
from .serializers import ListProductSerializer , CreateProductSerializer , DetailProductSerializer 
from rest_framework.permissions import IsAuthenticated 
from .permissions import  IsOwnerOrReadOnly
from rest_framework.views import APIView , Response 
from rest_framework import status 
from django.http import Http404 , HttpResponseNotFound

# Product Views
class ListActiveProductsView(ListAPIView):
    queryset = Product.objects.filter(status = 'True')
    serializer_class = ListProductSerializer
    permission_classes = (IsAuthenticated , )


class ListAllProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer
    permission_classes = (IsAuthenticated , )


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes = (IsAuthenticated , )

class DetailProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = DetailProductSerializer
    permission_classes = (IsOwnerOrReadOnly , IsAuthenticated )