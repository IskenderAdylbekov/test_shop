from django.contrib import admin

from .models import Category, Tag, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "created_at")
    list_filter = ("category", "tags")
    search_fields = ("name", "description")
    filter_horizontal = ("tags",)


admin.site.register(Category)
admin.site.register(Tag)
