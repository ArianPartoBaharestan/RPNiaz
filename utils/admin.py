from django.contrib import admin
from .models import Images



# Image model

# class ProductAdmin(admin.ModelAdmin):
#     list_filter = ['category']

admin.site.register(Images)