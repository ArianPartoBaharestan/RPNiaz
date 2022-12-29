from django.contrib import admin

# Register your models here.
from .models import Images , Product


# Image model
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'image_tag']


# class ProductAdmin(admin.ModelAdmin):
#     list_filter = ['category']

admin.site.register(Images, ImageAdmin)
admin.site.register(Product)