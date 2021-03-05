from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Product


def index_view(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={'products': products})