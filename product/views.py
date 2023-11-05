from django.db.models import Avg, Max, Min
from django.shortcuts import render, get_object_or_404

from product.models import Product


# Create your views here.
def product_list(request):
    all_product=Product.objects.all()
    return render(request,'product/product_list.html',{'all_products':all_product})


def product_details(request,slug):
    products = get_object_or_404(Product,slug=slug)
    return render(request,'product/product_details.html',{'product':products})