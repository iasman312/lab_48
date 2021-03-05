from django.db import models
from django.core.validators import MinValueValidator

category_choices = [('smartphone', 'Смартфон'), ('laptop', 'Ноутбук'),
                    ('camera', 'Камера'), ('other', 'Разное')]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False,
                            verbose_name="Название товара")
    description = models.TextField(max_length=2000, null=True, blank=True,
                                   verbose_name="Описание товара")
    category = models.CharField(max_length=100, choices=category_choices,
                                default="other", verbose_name="Категория")
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
