# Generated by Django 4.1.2 on 2023-01-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.UUIDField(default='5226d217efbb41da9af63418c1dd82fe', editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ایدی'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default='5226d217efbb41da9af63418c1dd82fe', editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ایدی'),
        ),
    ]
