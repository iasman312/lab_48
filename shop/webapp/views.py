from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Product
from .forms import ProductForm, SearchForm


def index_view(request):
    form = SearchForm()
    if request.GET.get('name'):
        products = Product.objects.all().order_by('category', 'name').exclude(
            balance=0).filter(name__startswith=request.GET.get('name'))
        return render(request, 'index.html', context={'products': products,
                                                      'form': form})
    products = Product.objects.all().order_by('category', 'name').exclude(
        balance=0)
    return render(request, 'index.html', context={'products': products,
                                                  'form': form})


def product_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product_view.html', context={'product': product})


def product_create_view(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'product_create.html', context={'form': form})
    elif request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            article = Product.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                category=form.cleaned_data.get('category'),
                balance=form.cleaned_data.get('balance'),
                price=form.cleaned_data.get('price')
            )
            return redirect('product-view', pk=article.id)
        return render(request, 'product_create.html', context={'form': form})


def product_update_view(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == 'GET':
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'balance': product.balance,
            'price': product.price
        })
        return render(request, 'product_update.html', context={'form': form,
                                                               'product':
                                                                   product})

    elif request.method == 'POST':
        form = ProductForm(
            data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get('description')
            product.category = form.cleaned_data.get('category')
            product.balance = form.cleaned_data.get('balance')
            product.price = form.cleaned_data.get('price')
            product.save()
            return redirect('product-view',
                            pk=product.id)

        return render(request, 'product_create.html',
                      context={'form': form, 'product': product})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, id=pk)  # получаем статью

    if request.method == 'GET':
        return render(request, 'product_delete.html', context={'product':
                                                               product})
    elif request.method == 'POST':
        product.delete()
        return redirect('product-list')
