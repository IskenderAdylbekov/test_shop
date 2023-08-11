from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # Механизм инвалидации кеша при обновлении или создании новых товаров.

    @classmethod
    @receiver(post_save, sender="products.Product")
    def invalidate_product_cache(sender, instance, **kwargs):
        cache_key = "product_list"
        cache.delete(cache_key)
