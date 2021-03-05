from django.urls import path
from webapp.views import (
    index_view,
    product_view,
    product_create_view,
    product_update_view
)

urlpatterns = [
    path('', index_view, name='product-list'),
    path('add/', product_create_view, name='product-add'),
    path('<int:pk>/', product_view, name='product-view'),
    path('<int:pk>/update', product_update_view, name='product-update'),
]