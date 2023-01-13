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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        if data['parent'] in Comment.objects.filter(Blog = data['Blog']) or  data['parent'] == None:
            return data
        else:
            raise serializers.ValidationError('parent most be in blog')
=======
        if data['parent'] in Comment.objects.filter(Blog = data['Blog']) or data['parent'] == None:
            return data
        else:
            raise serializers.ValidationError('parent most be in blog')

>>>>>>> Stashed changes
=======
        if data['parent'] in Comment.objects.filter(Blog = data['Blog']) or data['parent'] == None:
            return data
        else:
            raise serializers.ValidationError('parent most be in blog')

>>>>>>> Stashed changes
        
    class Meta:
        model = Comment
        exclude = ('published' ,)

    def create(self, validated_data):
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        obj = Comment()
        obj.Blog = validated_data.get('Blog')
        obj.user = self.context['request'].user
        obj.text = validated_data.get('text')
        obj.parent = validated_data.get('parent')
        obj.save()
        return obj
=======
=======
>>>>>>> Stashed changes
        comment = Comment()
        comment.Blog = validated_data.get('Blog')
        comment.user = self.context['request'].user
        comment.parent = validated_data.get('parent')
        comment.text = validated_data.get('text')
        comment.save()
<<<<<<< Updated upstream
        return comment
>>>>>>> Stashed changes
=======
        return comment
>>>>>>> Stashed changes
