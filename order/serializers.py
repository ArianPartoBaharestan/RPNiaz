from rest_framework import serializers
from .models import Basket, OrderItem
from product.serializer import ListProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ListProductSerializer(read_only=True)


    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']


class BasketSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, basket):
        return sum([item.quantity * item.product.price for item in basket.items.all()])

    class Meta:
        model = Basket
        fields = ['id', 'items', 'total_price']
