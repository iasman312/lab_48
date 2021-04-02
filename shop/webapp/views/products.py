from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode

from webapp.models import Product, Category
from webapp.forms import ProductForm, SearchForm


class IndexView(ListView):
    template_name = 'products/index.html'
    model = Product
    context_object_name = 'products'
    ordering = ('category', 'name')
    paginate_by = 5
    paginate_orphans = 2

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(IndexView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset.exclude(balance=0)

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        context['categories'] = Category.objects.all()

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class ProductByCategory(ListView):
    template_name = 'products/by_category.html'
    model = Product
    context_object_name = 'products_by_category'
    ordering = ('name')
    paginate_by = 5
    paginate_orphans = 2

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(ProductByCategory, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset.exclude(balance=0).filter(category=self.kwargs.get('selected_category'))

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class ProductView(DetailView):
    model = Product
    template_name = 'products/view.html'


class CreateProductView(CreateView):
    template_name = 'products/create.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        product = Product()
        for key, value in form.cleaned_data.items():
            setattr(product, key, value)
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'products/update.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product-view', kwargs={'pk': self.kwargs.get('pk')})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product-list')


