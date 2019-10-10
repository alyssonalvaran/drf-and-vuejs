from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product, Manufacturer


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_details.html"