# Generated by Django 4.1.2 on 2023-01-04 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import product.helper


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='موضوع')),
                ('body', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to=product.helper.upload_image_path, verbose_name='تصویر اگهی')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='عبارت لینک')),
                ('status', models.CharField(choices=[('True', 'منتشر شده'), ('False', 'در انتظار تایید'), ('Destroy', 'رد شده')], max_length=30, verbose_name='وضعیت اگهی')),
                ('creat_at', models.DateTimeField(auto_now_add=True, verbose_name='ایجاده شده در تاریخ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در تاریخ')),
                ('publish_at', models.DateTimeField(blank=True, null=True, verbose_name='زمان انتشار')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='متن')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
