# Generated by Django 4.1.2 on 2023-01-08 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import utils.api.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.UUIDField(default='456525358dda482cba9e14a3c39eb2de', editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ایدی')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
                ('title', models.CharField(max_length=200, verbose_name='موضوع')),
                ('body', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to=utils.api.utils.upload_image_path, verbose_name='تصویر اگهی')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='عبارت لینک')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در تاریخ')),
                ('publish_at', models.DateTimeField(blank=True, null=True, verbose_name='زمان انتشار')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default='456525358dda482cba9e14a3c39eb2de', editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ایدی')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
                ('text', models.TextField(verbose_name='متن')),
                ('published', models.BooleanField(default=False)),
                ('Blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='blog.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]