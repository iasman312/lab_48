from django.urls import path
from webapp.views import (
    index_view,
    product_view,
    product_create_view,
    product_update_view,
    product_delete_view,
    product_category_view,
)

urlpatterns = [
    path('', index_view, name='product-list'),
    path('add/', product_create_view, name='product-add'),
    path('<int:pk>/', product_view, name='product-view'),
    path('<int:pk>/update', product_update_view, name='product-update'),
    path('<int:pk>/delete', product_delete_view, name='product-delete'),
    path('<str:selected_category>/', product_category_view,
         name='product-category'),
]