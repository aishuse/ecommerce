from django.db import models

from authapp.models import User
from ecommerce.common.abstract_models import Abstractmodels
from admins.models import Category


class Product(Abstractmodels):
    name = models.CharField(max_length=120, verbose_name='Product Name')
    brand = models.CharField(max_length=120, verbose_name='Brand Name', blank=True)
    price = models.PositiveIntegerField(default=0)
    details = models.CharField(max_length=1000, verbose_name='Details of Product')
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class ProductStock(Abstractmodels):
    stock_available = models.PositiveIntegerField(default=0, help_text='No: of Product Available')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productstock')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stockadder')

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return str(self.product)