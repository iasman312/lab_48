from rest_framework import generics

from api_v1.serializers.order import OrderSerializer
from webapp.models import Order


class OrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer