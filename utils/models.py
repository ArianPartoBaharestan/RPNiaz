from django.db import models
from .api.utils import upload_image_path
from uuid import uuid4
from datetime import datetime
from django.utils import timezone

class AbstracId(models.Model):
    id = models.UUIDField(verbose_name='ایدی' , primary_key=True , editable= False , unique= True , default= uuid4) 
    create_at = models.DateTimeField(verbose_name='زمان ایجاد' ,default= timezone.now)




class Images(AbstracId , models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='عنوان')
    image = models.ImageField(blank=True, upload_to=upload_image_path, verbose_name='تصویر')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'
