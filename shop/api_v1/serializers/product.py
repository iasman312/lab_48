from rest_framework import serializers

from webapp.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'balance', 'price')