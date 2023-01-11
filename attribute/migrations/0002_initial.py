# Generated by Django 4.1.5 on 2023-01-11 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('category', '0001_initial'),
        ('attribute', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattribute',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='attributeitem',
            name='Attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.attribute'),
        ),
        migrations.AddField(
            model_name='attributegroup',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute_group', to='category.category'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='Attribute_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.attributegroup', verbose_name='attribute'),
        ),
    ]
