from django.urls import path
from .views import product_list, product_details

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
]