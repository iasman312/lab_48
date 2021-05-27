from rest_framework import serializers

from webapp.models import Order, ProductOrder


class ProductOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductOrder
        fields = ('id', 'product', 'quantity', 'order')
        read_only_fields = ('id', 'order')


class OrderSerializer(serializers.ModelSerializer):
    order_products = ProductOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'tel_number', 'address', 'created_at', 'order_products')
        read_only_fields = ('id',)

    def create(self, validated_data):
        order = Order()
        setattr(order, 'tel_number', validated_data['tel_number'])
        setattr(order, 'address', validated_data['address'])
        order.save()
        for product in validated_data['order_products']:
            order_products = ProductOrder()
            setattr(order_products, 'product', product['product'])
            setattr(order_products, 'quantity', product['quantity'])
            setattr(order_products, 'order', order)
            order_products.save()
        return validated_data


