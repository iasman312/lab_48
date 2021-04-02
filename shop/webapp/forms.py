from django import forms
from django.forms import widgets
from webapp.models import Product, Order


class ProductForm(forms.ModelForm):
    """
    Форма для создания и редактирваония объектов статьи
    https://docs.djangoproject.com/en/3.1/ref/forms/
    """
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'balance', 'price')


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти '
                                                                    'товар')


class OrderForm(forms.Form):
    class Meta:
        model = Order
        fields = ('user_name', 'tel_number', 'address')
