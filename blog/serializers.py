from rest_framework import serializers
from .models import Blog , Comment
from product.models import Product

class ListBlogSerializer(serializers.ModelSerializer):
    def get_owner(self , obj):
        return obj.owner.phone

    owner  = serializers.SerializerMethodField(method_name='get_owner')
    # slug = serializers.Hyperlink()
    class Meta:
        model = Blog 
        fields = '__all__'

class CreateBlogSerializer(serializers.ModelSerializer):
    
    product = serializers.PrimaryKeyRelatedField(queryset = Product.objects.filter(status = True))
    class Meta:
        model = Blog
        fields = ('product' ,'title' , 'body' , 'image' , 'status' , 'slug' )

    def create(self, validated_data):
        blog = Blog()
        owner = self.context['request'].user
        blog.owner = owner
        blog.product = validated_data.get('product')
        blog.title = validated_data.get('title')
        blog.body = validated_data.get('body')
        blog.image = validated_data.get('image')
        blog.status = validated_data.get('status')
        blog.creat_at = validated_data.get('creat_at')
        blog.update_at = validated_data.get('update_at')
        blog.publish_at = validated_data.get('publish_at')
        blog.save()
        return blog

class RetriveUpdateDestroyBlogSerializer(serializers.ModelSerializer):

    def get_owner(self , obj):
        return obj.owner.phone

    owner  = serializers.SerializerMethodField(method_name='get_owner')
    class Meta:
        model = Blog
        fields = '__all__'