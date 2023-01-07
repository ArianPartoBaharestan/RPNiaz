from django.db import models
from authentication.models import User
import random
import os
from category.models import Category , Brand
from utils.models import AbstracId


# This part for Product DataBase


class Product(AbstracId ,models.Model):

    STATUS = (
        ('True', "فعال"),
        ("False", "غیرفعال")
    )

    TYPE = (
        ('New' , 'نو') ,
        ('Used-good' , 'در حد نو') ,
        ('Old' , 'کهنه') ,
    )

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='دسته')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='برند')
    title = models.CharField(max_length=200, verbose_name='عنوان فارسی')
    title_eng = models.CharField(max_length=150, blank=True, null=True, verbose_name='عنوان انگلیسی')
    keyword = models.CharField(max_length=250, verbose_name='کلمه کلیدی')
    description = models.CharField(max_length=300, verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    amount = models.IntegerField(verbose_name='تعداد')
    status = models.CharField(max_length=50, choices=STATUS,default= False ,verbose_name='وضعیت')
    product_status = models.CharField(max_length = 50 , choices= TYPE ,verbose_name = "کیفیت کالا" )
    slug = models.SlugField(verbose_name='عبارت لینک', null=False, unique=True, allow_unicode=True, max_length=200)
    creat_at = models.DateTimeField(auto_now_add=True, verbose_name='ایجاده شده در تاریخ')
    update_at = models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در تاریخ')
    change = models.BooleanField(verbose_name = 'قابل معاوضه' , default= False)
    seller = models.ForeignKey(User , on_delete=models.CASCADE  , related_name= 'seller' )
    # objects = ProductsManager()


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

