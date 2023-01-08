from django.db import models
from utils.models import AbstracId, Images


class Configure(AbstracId, models.Model):
    web_title = models.CharField(max_length=255, verbose_name='موضوع سایت')
    nav_icon = models.ForeignKey(Images, null=True, blank=True, on_delete=models.CASCADE)
    site_description = models.CharField(max_length=255, verbose_name='توضیحات سایت')
    fav_icon = models.ForeignKey(Images, null=True, blank=True, on_delete=models.CASCADE)
