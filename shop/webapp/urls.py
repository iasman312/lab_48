from django.urls import path
from webapp.views import IndexView, ProductView, CreateProductView, \
    ProductUpdateView, ProductDeleteView, ProductByCategory

urlpatterns = [
    path('', IndexView.as_view(), name='product-list'),
    path('add/', CreateProductView.as_view(), name='product-add'),
    path('<int:pk>/', ProductView.as_view(), name='product-view'),
    path('<int:pk>/update/', ProductUpdateView.as_view(),
         name='product-update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(),
         name='product-delete'),
    path('<str:selected_category>/', ProductByCategory.as_view(),
         name='product-category'),
]