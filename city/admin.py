from django.contrib import admin
from .models import Province, City
from django.contrib.admin import ModelAdmin

class CityAdmin(ModelAdmin):
    list_display = ('id' , 'name') 

admin.site.register(Province)
admin.site.register(City , CityAdmin)
