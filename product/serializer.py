from rest_framework import serializers
from .models import Product , Images
from authentication.models import User

class ListProductSerializer(serializers.ModelSerializer):
    # category = 
    # brand = 

    class Meta:
        model = Product
        fields = '__all__'


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class DetailProductSerializer(serializers.ModelSerializer):
    def get_seller(self , obj):
        return obj.seller.phone

    seller = serializers.SerializerMethodField(method_name='get_seller')
    class Meta:
        model = Product
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'