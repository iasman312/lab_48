from django.urls import path
from webapp.views import IndexView, ProductView, CreateProductView, \
    ProductUpdateView, ProductDeleteView, ProductByCategory, ProductToCart, \
    CartView, CartDeleteView, CartOrderView, OrderListView, stats_view

urlpatterns = [
    path('', IndexView.as_view(), name='product-list'),
    path('add/', CreateProductView.as_view(), name='product-add'),
    path('<int:pk>/', ProductView.as_view(), name='product-view'),
    path('<int:pk>/update/', ProductUpdateView.as_view(),
         name='product-update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(),
         name='product-delete'),
    path('category/<str:selected_category>/', ProductByCategory.as_view(),
         name='product-category'),
    path('<int:pk>/cart/', ProductToCart.as_view(), name='product-in-cart'),
    path('cart/', CartView.as_view(), name='cart-view'),
    path('cart/<int:pk>/delete/', CartDeleteView.as_view(), name='cart-delete'),
    path('cart/order/', CartOrderView.as_view(), name='cart-order'),
    path('order_list/', OrderListView.as_view(), name='order-list'),
    path('statistics/', stats_view, name='stats')
]