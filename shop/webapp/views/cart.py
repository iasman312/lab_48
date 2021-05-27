from django.views.generic import (
    CreateView
)
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.base import View

from webapp.mixins import HitsMixin
from webapp.models import Product, Cart, Order
from webapp.forms import OrderForm
from django.contrib import messages


class ProductToCart(View):
    def get(self, request, pk):
        my_dict = request.session.get('my_dict', [])
        product = Product.objects.get(pk=pk)
        qty = int(request.GET.get('quantity'))
        if product.balance < 1:
            return redirect('product-list')
        try:
            if qty <= product.balance:
                cart = Cart.objects.get(product__pk=pk, pk__in=my_dict)
                cart.quantity += qty
                cart.save()
                product.balance -= qty
                product.save()
                message_content = f'Добавили "{product.name}" {qty} штуки!'
                messages.success(self.request, message_content)
            else:
                message_content = f'Не смогли добавить "{product.name}"'
                messages.error(self.request, message_content)
        except:
            if qty <= product.balance:
                cart = Cart.objects.create(product=product, quantity=qty)
                my_dict.append(cart.pk)
                product.balance -= qty
                product.save()
                message_content = f'Добавили "{product.name}" {qty} штуки!'
                messages.success(self.request, message_content)
            else:
                message_content = f'Не смогли добавить "{product.name}"'
                messages.error(self.request, message_content)

        request.session['my_dict'] = my_dict

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class CartView(HitsMixin, CreateView):
    template_name = 'cart/index.html'
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('product-list')

    def get_context_data(self, **kwargs):
        my_dict = self.request.session.get('my_dict', [])
        total = 0
        for i in my_dict:
            cart = Cart.objects.get(pk=i)
            total += cart.product.price * cart.quantity
        kwargs['total'] = total
        kwargs['cart_items'] = Cart.objects.filter(pk__in=my_dict)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


class CartDeleteView(View):
    def get(self, request, *args, **kwargs):
        my_dict = request.session.get('my_dict', [])
        cart = Cart.objects.get(pk=kwargs.get('pk'))
        product = Product.objects.get(pk=cart.product.pk)
        if cart.quantity == 1:
            my_dict.remove(cart.pk)
            cart.delete()
        else:
            cart.quantity -= 1
            cart.save()
        product.balance += 1
        product.save()
        request.session['my_dict'] = my_dict
        message_content = f'Удалили "{product.name}" 1 штуку!'
        messages.success(self.request, message_content)
        return redirect('cart-view')



