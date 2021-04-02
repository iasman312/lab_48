from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic.base import View

from webapp.models import Product, Category, Cart
from webapp.forms import ProductForm, SearchForm


class ProductToCart(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        if product.balance < 1:
            return redirect('product-list')
        try:
            cart = Cart.objects.get(product__pk=pk)
            cart.quantity += 1
            product.balance -= 1
            cart.save()
            product.save()
        except:
            Cart.objects.create(product=product, quantity=1)
            product.balance -= 1
            product.save()

        return redirect('product-list')


class CartView(ListView):
    template_name = 'cart/index.html'
    model = Cart
    context_object_name = 'cart_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        for i in Cart.objects.all():
            total += i.product.price * i.quantity
        context['total'] = total
        return context


class CartDeleteView(DeleteView):
    model = Cart
    success_url = reverse_lazy('cart-view')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



