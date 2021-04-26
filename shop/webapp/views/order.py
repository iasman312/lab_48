from django.views.generic import (
    ListView
)
from django.shortcuts import render, redirect
from django.views.generic.base import View

from webapp.models import Cart, Order, ProductOrder
from webapp.forms import OrderForm


class CartOrderView(View):
    def post(self, request):
        my_dict = request.session.get('my_dict')
        form = OrderForm(data=request.POST)
        if form.is_valid():
            order = form.save()
            for i in my_dict:
                cart = Cart.objects.get(pk=i)
                product = ProductOrder.objects.create(product=cart.product,
                                                      order=order, quantity=cart.quantity)
                if request.user.is_authenticated:
                    order.user = request.user
                    order.save()
            request.session.pop('my_dict')
            return redirect('product-list')
        else:
            return render(request, 'cart/index.html', context={'form': form,
                                                               'cart': my_dict})


class OrderListView(ListView):
    template_name = 'order/order_list.html'
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        queryset = queryset.filter(user__pk=self.request.user.pk)
        return queryset
