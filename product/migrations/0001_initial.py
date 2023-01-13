# Generated by Django 4.1.2 on 2023-01-09 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ایدی')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان فارسی')),
                ('title_eng', models.CharField(blank=True, max_length=150, null=True, verbose_name='عنوان انگلیسی')),
                ('keyword', models.CharField(max_length=250, verbose_name='کلمه کلیدی')),
                ('description', models.CharField(max_length=300, verbose_name='توضیحات')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('amount', models.IntegerField(verbose_name='تعداد')),
                ('status', models.CharField(choices=[('True', 'فعال'), ('False', 'غیرفعال')], default=False, max_length=50, verbose_name='وضعیت')),
                ('product_status', models.CharField(choices=[('New', 'نو'), ('Used-good', 'در حد نو'), ('Old', 'کهنه')], max_length=50, verbose_name='کیفیت کالا')),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, null=True, unique=True, verbose_name='عبارت لینک')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در تاریخ')),
                ('change', models.BooleanField(default=False, verbose_name='قابل معاوضه')),
                ('Brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.brand', verbose_name='برند')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='دسته')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city.city', verbose_name='شهر')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ایدی')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.images')),
                ('productt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'تصویر محصول',
                'verbose_name_plural': ' تصاویر محصول',
            },
        ),
    ]
