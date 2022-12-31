from rest_framework import serializers
from .models import Product , Images
from authentication.models import User
from category.models import Category , Brand


class CategoryDetailSerializer(serializers.ModelSerializer):
    def get_parent(self , obj):
        return (obj.parent.title , obj.parent.parent)
    parent = serializers.SerializerMethodField(method_name= 'get_parent')
    class Meta :
        model = Category
        fields = ('title' , 'parent' , 'keyword' , 'slug')

class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ListProductSerializer(serializers.ModelSerializer):

    category = CategoryDetailSerializer() 
    brand = BrandDetailSerializer()
    class Meta:
        model = Product
        fields = '__all__'


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['seller']
    def create(self, validated_data):
        obj = Product()
        obj.category = validated_data.get('category')
        obj.brand = validated_data.get('brand')
        obj.title= validated_data.get('title')
        obj.keyword = validated_data.get('keyword')
        obj.description = validated_data.get('description')
        obj.price = validated_data.get('price')
        obj.amount = validated_data.get('amount')
        obj.status = validated_data.get('status')
        obj.product_status = validated_data.get('product_status')
        obj.slug = validated_data.get('slug')
        obj.seller = self.context.get('request').user
        if validated_data.get('title_eng'):
            obj.title_eng = validated_data.get('title_eng')

        if validated_data.get('change'):
            obj.change = validated_data.get('change')
        obj.save()
        return obj
        
class DetailProductSerializer(serializers.ModelSerializer):
    def get_seller(self , obj):
        return obj.seller.phone

    category = CategoryDetailSerializer() 
    brand = BrandDetailSerializer()
    seller = serializers.SerializerMethodField(method_name='get_seller')
    class Meta:
        model = Product
        fields = '__all__'

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

    
