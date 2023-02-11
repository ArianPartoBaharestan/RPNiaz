# Generated by Django 4.1.5 on 2023-02-06 16:07

from django.db import migrations, models
import django.utils.timezone
import storages.backends.ftp
import utils.api.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ایدی')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('image', models.ImageField(storage=storages.backends.ftp.FTPStorage(), upload_to=utils.api.utils.upload_image_path, verbose_name='تصویر')),
                ('alt', models.CharField(blank=True, max_length=50, null=True, verbose_name='seo alt')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصاویر',
            },
        ),
    ]
