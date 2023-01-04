from django.shortcuts import render
from .models import Blog , Comment
from rest_framework import generics
from .serializers import ListBlogSerializer , CreateBlogSerializer , RetriveUpdateDestroyBlogSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class ListActiveBlogView(generics.ListAPIView):
    queryset = Blog.objects.filter(product__status = True , status = True)
    serializer_class = ListBlogSerializer
    permission_classes = ( IsAuthenticatedOrReadOnly , )


class ListDestroyBlogView(generics.ListAPIView):
    queryset = Blog.objects.filter(status = 'Destroy')
    serializer_class = ListBlogSerializer
    permission_classes = ( IsAuthenticatedOrReadOnly , )


class ListWaitingBlogView(generics.ListAPIView):
    queryset = Blog.objects.filter(status = 'Destroy')
    serializer_class = ListBlogSerializer
    permission_classes = ( IsAuthenticatedOrReadOnly , )


class CreateBlogView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = CreateBlogSerializer
    permission_classes = (IsAuthenticated , )


class RetriveUpdateDestroyBlogView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Blog.objects.all()
    serializer_class = RetriveUpdateDestroyBlogSerializer
    permission_classes = (IsOwnerOrReadOnly , IsAuthenticated , )