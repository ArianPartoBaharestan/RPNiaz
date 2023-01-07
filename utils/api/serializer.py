from rest_framework import serializers
from utils.models import Images


class ListImageSerializer(serializers.ModelSerializer):
    def get_product(self , obj):
        return obj.product.title
    product = serializers.SerializerMethodField(method_name='get_product')
    class Meta:
        model = Images
        fields = '__all__'


class CreateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

    
