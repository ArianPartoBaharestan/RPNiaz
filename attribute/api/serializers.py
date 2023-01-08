from rest_framework import serializers
from attribute.models import AttributeGroup, Attribute, AttributeItem, ProductAttribute


class AttributeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeGroup
        fields = '__all__'


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'


class AttributeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeItem
        fields = '__all__'


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = '__all__'
