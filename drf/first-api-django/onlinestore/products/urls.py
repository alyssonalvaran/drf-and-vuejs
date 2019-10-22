from django.urls import path
from .views import (product_list, product_details, 
                    manufacturer_list, manufacturer_details)

urlpatterns = [
    path(
        "products/",
        product_list,
        name="product-list"
    ),
    path(
        "products/<int:pk>/",
        product_details,
        name="product-details"
    ),
    path(
        "manufacturers/",
        manufacturer_list,
        name="manufacturer-list"
    ),
    path(
        "manufacturers/<int:pk>/",
        manufacturer_details,
        name="manufacturer-details"
    ),
]