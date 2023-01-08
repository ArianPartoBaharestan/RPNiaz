from django.db import models
from product.models import Product
from utils.models import AbstracId, Images
from category.models import Category


class AttributeGroup(AbstracId):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Attribute(AbstracId):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    attribute_type = models.CharField(max_length=50, verbose_name='نوع')
    Attribute_group = models.ForeignKey(AttributeGroup, on_delete=models.CASCADE)


class AttributeItem(AbstracId):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    Attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)


class ProductAttribute(AbstracId):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)