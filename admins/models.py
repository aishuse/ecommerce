
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name='product Category')

    def __str__(self):
        return self.name