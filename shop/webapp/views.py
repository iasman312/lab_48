from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Product


def index_view(request):
    products = Product.objects.all().order_by('category', 'name')
    return render(request, 'index.html', context={'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product_view.html', context={'product': product})