from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView , Response , status
from utils.models import Images
from .serializer import ListImageSerializer , CreateImageSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner



class ListImageView(APIView):
    def get(self , request , product):
        queryset = Images.objects.filter(product__title = product)
        serializer = ListImageSerializer(queryset , many = True)
        return Response(data = serializer.data  , status= status.HTTP_200_OK)

class CreateImageView(CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = CreateImageSerializer
    # permission_classes = (IsAuthenticated , )

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
    permission_classes = (IsOwner , )