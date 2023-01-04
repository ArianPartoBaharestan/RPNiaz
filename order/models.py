from django.db import models
from uuid import uuid4
from authentication.models import User
from product.models import Product


class Basket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'سبدکالا'
        verbose_name_plural = 'سبد های کالا'


class OrderItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.basket.id}"

    class Meta:
        unique_together = [['basket', 'product']]
        verbose_name = 'خرید'
        verbose_name_plural = 'خرید ها'
