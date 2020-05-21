""" mainapp models
"""
from django.urls import reverse
from django.db import models

# Create your models here.

class Category(models.Model):
    """ product category model
    """
    slug = models.SlugField(max_length=30, unique=True, verbose_name='имя для URL')
    name = models.CharField(max_length=60, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    class Meta:
        ordering = ('name',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    """ product model
    """
    slug = models.SlugField(max_length=30, verbose_name='имя для URL')
    name = models.CharField(max_length=120, verbose_name='название')
    image = models.ImageField(upload_to='product_img', verbose_name='фото товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(verbose_name='описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='цена')

    class Meta:
        unique_together = ('category', 'slug',)
        ordering = ('category', 'name',)
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'mainapp:catalog:product',
            kwargs={'category': self.category.slug, 'product': self.slug}
        )
