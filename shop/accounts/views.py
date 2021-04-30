from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from accounts.forms import MyUserCreationForm
from webapp.models import Cart, Product


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product-list')
    else:
        form = MyUserCreationForm()
    return render(request, 'user_create.html', context={'form': form})


class MyLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        session = self.request.session.get('my_dict', [])
        carts = Cart.objects.filter(pk__in=session)
        if carts:
            for cart in carts:
                product = Product.objects.get(pk=cart.product.pk)
                product.balance += cart.quantity
                product.save()
                cart.delete()
        return super().dispatch(request, *args, **kwargs)