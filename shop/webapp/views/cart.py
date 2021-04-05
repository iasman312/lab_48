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

from webapp.models import Product, Category, Cart, Order
from webapp.forms import ProductForm, SearchForm, OrderForm


class ProductToCart(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        qty = int(request.GET.get('quantity'))
        if product.balance < 1:
            return redirect('product-list')
        try:
            cart = Cart.objects.get(product__pk=pk)
            if qty <= product.balance:
                cart.quantity += qty
                product.balance -= qty
                cart.save()
                product.save()
        except:
            if qty <= product.balance:
                Cart.objects.create(product=product, quantity=qty)
                product.balance -= qty
                product.save()

        return redirect('product-list')


class CartView(CreateView):
    template_name = 'cart/index.html'
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('product-list')

    def get_context_data(self, **kwargs):
        total = 0
        for i in Cart.objects.all():
            total += i.product.price * i.quantity
        kwargs['total'] = total
        kwargs['cart_items'] = Cart.objects.all()
        print(kwargs)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):

        return super().form_valid(form)


class CartDeleteView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(pk=kwargs.get('pk'))
        product = Product.objects.get(pk=cart.product.pk)
        if cart.quantity == 1:
            cart.delete()
        else:
            cart.quantity -= 1
            cart.save()
        product.balance += 1
        product.save()

        return redirect('cart-view')



