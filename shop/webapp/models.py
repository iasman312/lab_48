from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False,
                            verbose_name="Название товара")
    description = models.TextField(max_length=2000, null=True, blank=True,
                                   verbose_name="Описание товара")
    category = models.ForeignKey('webapp.Category', related_name='products',
                                 verbose_name='Статус',
                                 on_delete=models.PROTECT)
    balance = models.IntegerField(validators=[MinValueValidator(0)],
                                  verbose_name="Остаток")
    price = models.DecimalField(max_digits=7, decimal_places=2,
                                verbose_name="Стоимость")

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.id}. {self.name}: {self.description}'


class Category(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False,
                            verbose_name='Название')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Cart(models.Model):
    product = models.ForeignKey('webapp.Product', related_name='cart',
                                 verbose_name='Корзина',
                                 on_delete=models.PROTECT)
    quantity = models.IntegerField(verbose_name='Количество')

    class Meta:
        db_table = 'carts'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Order(models.Model):
    user_name = models.CharField(max_length=120, null=False, blank=False,
                                 verbose_name="Имя пользователя")
    tel_number = models.CharField(max_length=100, null=False, blank=False,
                                  verbose_name="Номер телефона")
    address = models.CharField(max_length=150, null=False, blank=False,
                               verbose_name="Адрес")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), related_name='orders',
                             on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return(self.user_name)


class ProductOrder(models.Model):
    product = models.ForeignKey('webapp.Product',
                                related_name='product_orders',
                                on_delete=models.CASCADE, verbose_name='Товар')
    order = models.ForeignKey('webapp.Order', related_name='order_products',
                              on_delete=models.CASCADE, verbose_name='Заказ')
    quantity = models.IntegerField(blank=False, null=False,
                                   verbose_name='Количество')
    def __str__(self):
        return "{} | {}".format(self.product, self.order)


