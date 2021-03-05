from django.urls import path
from webapp.views import (index_view, product_view,)

urlpatterns = [
    path('', index_view, name='product-list'),
    path('<int:pk>/', product_view, name='product-view'),
]