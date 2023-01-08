# Generated by Django 4.1.2 on 2023-01-08 17:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configure',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ایدی')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
                ('web_title', models.CharField(max_length=255, verbose_name='موضوع سایت')),
                ('site_description', models.CharField(max_length=255, verbose_name='توضیحات سایت')),
                ('fav_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fac_icon', to='utils.images', verbose_name='فاو آیکون')),
                ('nav_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='van_icon', to='utils.images', verbose_name='ناو آیکون')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
    ]
