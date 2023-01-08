from rest_framework import serializers
from utils.models import Images


class ListImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class CreateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('title' , 'image')

    
