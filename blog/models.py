from django.db import models
from authentication.models import User
from uuid import uuid4
from django.utils.text import  slugify
from datetime import datetime


class Blog(models.Model):
    STATUS = (
        ('True' , 'منتشر شده'),
        ('False' , 'در انتظار تایید'),
        ('Destroy' , 'رد شده'),
    )
    owner = models.ForeignKey(User , on_delete=models.CASCADE , related_name= 'blog_owner')
    title = models.CharField(verbose_name= 'موضوع' , max_length = 200)
    body = models.TextField(verbose_name=  'توضیحات')
    slug = models.SlugField(verbose_name= 'عبارت لینک' , unique = True , null= True , blank= True)
    status = models.CharField(verbose_name= 'وضعیت اگهی' , choices=STATUS , max_length= 30) 
    creat_at = models.DateTimeField(auto_now_add=True, verbose_name='ایجاده شده در تاریخ')
    update_at = models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در تاریخ')
    publish_at = models.DateTimeField(verbose_name= 'زمان انتشار' , null= True , blank= True , )

    def save(self):
        value = self.title + '-' + uuid4().hex
        self.slug = slugify(value=value)
        if self.status == "True":
            self.publish_at = datetime.now()
        super(Blog , self).save()

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog , on_delete= models.CASCADE , related_name='comments')
    user = models.ForeignKey(User , on_delete= models.CASCADE , related_name= 'comments')
    text = models.TextField(verbose_name='متن')
    parent = models.ForeignKey('self' , on_delete= models.CASCADE , related_name= 'replies' , null= True , blank= True)
    create_at = models.DateTimeField(verbose_name='زمان ساخت' , auto_now_add=True)
 
    def __str__(self) -> str:
        return self.text[:20]