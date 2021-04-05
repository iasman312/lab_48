from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    View
)
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic.base import View

from webapp.models import Product, Category, Cart, Order, ProductOrder
from webapp.forms import ProductForm, SearchForm, OrderForm


class CartOrderView(View):
    def post(self, request):
        form = OrderForm(data=request.POST)
        cart_object = Cart.objects.all()
        if form.is_valid():
            order = form.save()
            for cart in cart_object:
                ProductOrder.objects.create(product=cart.product,
                                            order=order, quantity=cart.quantity)
            Cart.objects.all().delete()
            return redirect('product-list')
        else:
            return render(request, 'cart/index.html', context={'form': form,
                                                           'cart': cart_object})