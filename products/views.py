from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions
from django.http import HttpResponse
from openpyxl import Workbook
from django.contrib.auth.decorators import login_required
from django.core.cache import cache


from .models import Product
from .serializers import ProductSerializer
from .mixins import CachedListViewMixin


# @cache_page(60 * 15)  # Cache for 15 minutes
class ProductList(CachedListViewMixin, generics.ListCreateAPIView):
    queryset = Product.objects.select_related("category").prefetch_related("tags")
    serializer_class = ProductSerializer

    # Инвалидация кеша
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        self.invalidate_cache()
        return response

    def perform_update(self, serializer):
        response = super().perform_update(serializer)
        self.invalidate_cache()
        return response

    def invalidate_cache(self):
        cache_key = "product_list"
        cache.delete(cache_key)

    # def get_queryset(self):
    #     queryset = super().get_queryset()

    #     # This will ensure that related tags are prefetched
    #     return queryset

    # def get_queryset(self):
    #     # select_related и prefetch_related для оптимизации запросов

    #     # Fetch the product by ID only once
    #     product_id = self.request.query_params.get("product_id")
    #     product = get_object_or_404(Product, id=product_id)

    #     # Now you can reuse the 'product' variable as needed in your view logic
    #     # ...

    #     # Return the queryset (if applicable)
    #     queryset = Product.objects.all()
    #     return queryset

    #     queryset = (
    #         Product.objects.select_related("category")
    #         .prefetch_related("tags")
    #         .only("name", "description", "category__name", "price")
    #     )

    #     return queryset


class ProductDetail(CachedListViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related("category").prefetch_related("tags")
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        queryset = super().get_queryset()

        # This will ensure that related tags are prefetched
        return queryset


@login_required
def export_products_to_excel(request):
    products = Product.objects.all()

    wb = Workbook()
    ws = wb.active

    # Create header row
    ws.append(["Name", "Description", "Category", "Price"])

    # Populate rows with product data
    for product in products:
        ws.append(
            [
                product.name,
                product.description,
                product.category.name,
                product.price,
            ]
        )

    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = "attachment; filename=products.xlsx"

    wb.save(response)
    return response


class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        self.invalidate_cache()
        return response

    def perform_update(self, serializer):
        response = super().perform_update(serializer)
        self.invalidate_cache()
        return response

    def invalidate_cache(self):
        cache_key = "product_list"
        cache.delete(cache_key)
