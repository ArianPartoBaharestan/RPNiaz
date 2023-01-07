import random
from django.db import models
from django.utils.text import slugify
import os
from django.urls import reverse
import uuid


class BaseAbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


# برای آپلود عکس و درست کردن آدرسش
def upload_image_path(instance, filename):
    new_id = random.randint(1, 999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_id}-{instance.title}{ext}"
    return f"category/{final_name}"


class Category(BaseAbstractModel):
    STATUS = (
        ('True', "فعال"),
        ("False", "غیرفعال")
    )
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL,
                            verbose_name='دسته‌مادر')
    title = models.CharField(max_length=50, verbose_name='عنوان')
    en_title = models.CharField(max_length=50, verbose_name='عنوان انگلیسی')
    keyword = models.CharField(max_length=250, verbose_name='کلمه کلیدی')
    description = models.CharField(max_length=300, verbose_name='توضیحات')
    status = models.CharField(max_length=50, choices=STATUS, verbose_name='وضعیت')
    image = models.ImageField(blank=True, upload_to=upload_image_path, verbose_name='تصویر')
    slug = models.SlugField(verbose_name='عبارت لینک', blank=True, null=False, unique=True, allow_unicode=True,
                            max_length=200)
    creat_at = models.DateTimeField(auto_now_add=True, verbose_name='ایجاده شده در تاریخ')
    update_at = models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در تاریخ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = 'دسته‌بندی‌'


    def get_absolute_url(self):
        return reverse('product_category_list', kwargs={'slug': self.slug})

    def category_active(self):
        return self.objects.filter(status=True)

    def save(self, *args, **kwargs):
        is_slug = bool(Category.objects.filter(slug=self.en_title))
        if self.slug == '':
            if is_slug:
                self.slug = slugify(self.en_title + str(self.id))
            else:
                self.slug = slugify(self.en_title)
        super().save(*args, **kwargs)


class Brand(BaseAbstractModel):
    name = models.CharField(max_length=50, verbose_name='نام برند')
    description = models.CharField(max_length=300, verbose_name='توضیحات')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'دسته‌بندی برند'

    def __str__(self):
        return self.name