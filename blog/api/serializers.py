from rest_framework import serializers
from blog.models import Blog , Comment
from product.models import Product

class ListBlogSerializer(serializers.ModelSerializer):
    def get_owner(self , obj):
        return obj.owner.phone

    owner  = serializers.SerializerMethodField(method_name='get_owner')
    class Meta:
        model = Blog 
        fields = '__all__'

class RetriveUpdateDestroyBlogSerializer(serializers.ModelSerializer):

    def get_owner(self , obj):
        return obj.owner.phone

    owner  = serializers.SerializerMethodField(method_name='get_owner')
    class Meta:
        model = Blog
        fields = '__all__'


class ListCommentSerializer(serializers.ModelSerializer):
    def get_user(self  , obj):
        return obj.user.phone
    user = serializers.SerializerMethodField(method_name= 'get_user')    
    class Meta:
        model = Comment
        fields  = '__all__'


class CreateCommentSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['parent'] not in Comment.objects.filter(blog = data['blog']):
            raise serializers.ValidationError('parent most be in blog')
        return data
        
    class Meta:
        model = Comment
        exclude = ('published' ,)