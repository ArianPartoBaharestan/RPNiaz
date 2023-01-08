# Generated by Django 4.1.2 on 2023-01-08 17:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ایدی')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='نام استان')),
            ],
            options={
                'verbose_name': 'استان',
                'verbose_name_plural': 'استان ها',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ایدی')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
                ('name', models.CharField(max_length=50, verbose_name='نام شهر')),
                ('Province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='city.province', verbose_name='استان')),
            ],
            options={
                'verbose_name': 'شهر',
                'verbose_name_plural': 'شهر ها',
            },
        ),
    ]
