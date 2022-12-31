from .models import Product , Images
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveUpdateDestroyAPIView , ListCreateAPIView , DestroyAPIView
from .serializer import ListProductSerializer , CreateProductSerializer , DetailProductSerializer , ListImageSerializer , CreateImageSerializer
from rest_framework.permissions import IsAuthenticated 
from .permissions import IsOwner , IsOwnerOrReadOnly
from rest_framework.views import APIView , Response 
from rest_framework import status 
from django.http import Http404 , HttpResponseNotFound
# Product Views

class ListProductsView(ListAPIView):
    queryset = Product.objects.filter(status = 'True')
    serializer_class = ListProductSerializer
    permission_classes = (IsAuthenticated , )


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes = (IsOwner , )
# 
class DetailProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = DetailProductSerializer
    permission_classes = (IsOwnerOrReadOnly , )

class ListImageView(APIView):
    def get(self , request , product):
        print(product)
        queryset = Images.objects.filter(product__title = product)
        serializer = ListImageSerializer(queryset , many = True)
        return Response(data = serializer.data)
class CreateImageView(CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = CreateImageSerializer

class DeleteImageView(APIView):
    
    def get_object(self , pk):
        try:
            return Images.objects.get(id = pk)
        except Images.DoesNotExist:
            raise Http404   
    def delete(self, request , pk):
        image = self.get_object(pk=pk)
        image.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)