from django.urls import path

from .views import ProductList, ProductDetail, export_products_to_excel, ProductCreate

urlpatterns = [
    path("", ProductList.as_view(), name="product_list"),
    path("<int:pk>/", ProductDetail.as_view(), name="post_detail"),
    path("products/export/", export_products_to_excel, name="export_products_to_excel"),
    path("create/", ProductCreate.as_view(), name="product_create"),
]
