from django.db import models
from authentication.models import User
import random
import os
from category.models import Category , Brand
from django.utils.safestring import mark_safe


# This part for Product DataBase

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


# برای آپلود عکس و درست کردن آدرسش
def upload_image_path(instance, filename):
    new_id = random.randint(1, 999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_id}-{instance.title}{ext}"
    return f"gallery/{final_name}"


class Images(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='gallery',
                                verbose_name='محصول')
    title = models.CharField(max_length=50, blank=True, verbose_name='عنوان')
    image = models.ImageField(blank=True, upload_to=upload_image_path, verbose_name='تصویر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'تصویر'



# برای آپلود عکس و درست کردن آدرسش
def upload_image_path(instance, filename):
    new_id = random.randint(1, 999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_id}-{instance.title}{ext}"
    return f"products/{final_name}"


class Product(models.Model):

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
    # image = models.ImageField(upload_to=upload_image_path, verbose_name='تصویر')
    price = models.IntegerField(verbose_name='قیمت')
    amount = models.IntegerField(verbose_name='تعداد')
    status = models.CharField(max_length=50, choices=STATUS, verbose_name='وضعیت')
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

