from rest_framework import viewsets
from webapp.models import Product
from api_v1.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer