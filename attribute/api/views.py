from rest_framework import generics
from attribute.models import AttributeGroup, Attribute, AttributeItem, ProductAttribute
from .serializers import AttributeGroupSerializer, AttributeSerializer, AttributeItemSerializer, \
    ProductAttributeSerializer , CreateProductAttributeSerializer
from rest_framework.views import APIView

class AttributeGroupView(generics.ListAPIView):
    queryset = AttributeGroup.objects.all()
    serializer_class = AttributeGroupSerializer


class AttributeView(generics.ListAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class AttributeItemView(generics.ListAPIView):
    queryset = AttributeItem.objects.all()
    serializer_class = AttributeItemSerializer


class ProductAttributeView(generics.ListAPIView):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer

class CreateProductAttribute(generics.CreateAPIView):
    queryset = ProductAttribute.objects.all()
    serializer_class = CreateProductAttributeSerializer
    
# class CreateProductAttributeView(APIView):
#     def post(self , request , pk):
#         queryset = ProductAttribute.objects.filter(Product__id = pk )