from django import forms
from django.forms import widgets
from webapp.models import category_choices


class ProductForm(forms.Form):
    """
    Форма для создания и редактирваония объектов статьи
    https://docs.djangoproject.com/en/3.1/ref/forms/
    """
    name = forms.CharField(max_length=100, required=True, label='Название '
                                                                'товара')
    description = forms.CharField(max_length=1000, required=False,
                                  widget=widgets.Textarea, label='Описание '
                                  'товара')
    category = forms.ChoiceField(required=True, choices=category_choices,
                                 initial='other', label='Категория')
    balance = forms.IntegerField(min_value=0, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Цена')


class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label='Найти '
                                                                    'товар')
