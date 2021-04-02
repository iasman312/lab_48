from django.db import models
from django.core.validators import MinValueValidator

# category_choices = [('smartphone', 'Смартфон'), ('laptop', 'Ноутбук'),
#                     ('camera', 'Камера'), ('other', '')]


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
    product = models.ForeignKey('webapp.Category', related_name='cart',
                                 verbose_name='Корзина',
                                 on_delete=models.PROTECT)
    quantity = models.IntegerField(verbose_name='Количество')

    class Meta:
        db_table = 'carts'
        verbose_name = 'Корзина'
        verbose_name = 'Корзины'

