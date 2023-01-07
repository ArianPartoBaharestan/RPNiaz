# Generated by Django 4.1.4 on 2023-01-07 12:57

import category.models
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام برند')),
                ('description', models.CharField(max_length=300, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'برند',
                'verbose_name_plural': 'دسته\u200cبندی برند',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('en_title', models.CharField(max_length=50, verbose_name='عنوان انگلیسی')),
                ('keyword', models.CharField(max_length=250, verbose_name='کلمه کلیدی')),
                ('description', models.CharField(max_length=300, verbose_name='توضیحات')),
                ('status', models.CharField(choices=[('True', 'فعال'), ('False', 'غیرفعال')], max_length=50, verbose_name='وضعیت')),
                ('image', models.ImageField(blank=True, upload_to=category.models.upload_image_path, verbose_name='تصویر')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=200, unique=True, verbose_name='عبارت لینک')),
                ('creat_at', models.DateTimeField(auto_now_add=True, verbose_name='ایجاده شده در تاریخ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در تاریخ')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='category.category', verbose_name='دسته\u200cمادر')),
            ],
            options={
                'verbose_name': 'دسته',
                'verbose_name_plural': 'دسته\u200cبندی\u200c',
            },
        ),
    ]
