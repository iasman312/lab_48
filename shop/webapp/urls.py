from django.urls import path
from webapp.views import (index_view, product_view, product_create_view)

urlpatterns = [
    path('', index_view, name='product-list'),
    path('add/', product_create_view, name='product-add'),
    path('<int:pk>/', product_view, name='product-view'),
]