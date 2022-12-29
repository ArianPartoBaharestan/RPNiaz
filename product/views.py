from .models import Product , Images
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveUpdateDestroyAPIView , ListCreateAPIView
from .serializer import ListProductSerializer , CreateProductSerializer , DetailProductSerializer , ImageSerializer
from rest_framework.permissions import IsAuthenticated 
from .permissions import IsOwner , IsOwnerOrReadOnly

# Product Views

class ListProductsView(ListAPIView):
    queryset = Product.objects.filter(status = 'True')
    serializer_class = ListProductSerializer
    permission_classes = (IsAuthenticated , )


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes = (IsOwner , )

class DetailProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = DetailProductSerializer
    permission_classes = (IsOwnerOrReadOnly , )

class ListImageView(ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer