from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import Basket, OrderItem
from .serializers import BasketSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticated

class BasketViewSet(ModelViewSet):
    queryset = Basket.objects.prefetch_related('items__product').all()
    serializer_class = BasketSerializer
    # permission_classes = [IsAuthenticated]

class OrderItemViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return OrderItem.objects.filter(basket_id=self.kwargs['basket_pk']).select_related('product')
