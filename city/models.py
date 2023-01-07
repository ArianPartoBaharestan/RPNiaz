from django.db import models
from category.models import BaseAbstractModel

class Province(BaseAbstractModel):
    name = models.CharField(max_length=50, verbose_name="نام استان", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام شهر")
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name="استان", related_name="cities")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "شهر"
        verbose_name_plural = "شهر ها"