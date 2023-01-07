from django.db import models
from .api.utils import upload_image_path
from uuid import uuid4
from product.models import Product


class AbstracId(models.Model):
    id = models.CharField(verbose_name='id' , max_length= 40 , primary_key= True , default=uuid4().hex)

class Images(AbstracId , models.Model):
    product = models.ForeignKey(Product , on_delete=models.SET_NULL, null=True, related_name='gallery',
                                verbose_name='محصول')
    title = models.CharField(max_length=50, blank=True, verbose_name='عنوان')
    image = models.ImageField(blank=True, upload_to=upload_image_path, verbose_name='تصویر')
    create_at = models.DateTimeField(verbose_name='زمان ایجاد' , auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'
