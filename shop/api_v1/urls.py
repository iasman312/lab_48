from django.urls import include, path
from rest_framework import routers
from api_v1 import views
from api_v1.views import OrderView, CreateOrderView

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
    path('orders/', OrderView.as_view(), name='orders'),
    path('orders/create/', CreateOrderView.as_view(), name='order-create'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
