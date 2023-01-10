from rest_framework.generics import CreateAPIView , ListAPIView
from rest_framework.views import APIView , Response , status
from utils.models import Images
from .serializer import ListImageSerializer , CreateImageSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner



class ListImageView(ListAPIView):
    queryset = Images.objects.all()
    serializer = ListImageSerializer
    permission_classes = (IsAuthenticated , )


class CreateImageView(CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = CreateImageSerializer
    permission_classes = (IsAuthenticated , )

# class DeleteImageView(APIView):
#     def get_object(self , pk):
#         try:
#             return Images.objects.get(id = pk)
#         except Images.DoesNotExist:
#             raise Http404   

#     def delete(self, request , pk):
    
#         image = self.get_object(pk=pk)
#         image.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)
#     permission_classes = (IsOwner , )