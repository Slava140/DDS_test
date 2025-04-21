from datetime import datetime, timezone, date

from django.db import models
from django.db.models import ForeignKey


class Type(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название типа')

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    type = ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Тип операции')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название подкатегории')
    category = ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название статуса')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


def now():
    return datetime.now(timezone.utc)


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Сумма')
    comment = models.CharField(max_length=255, blank=True, verbose_name='Комментарий')
    created_on = models.DateField(null=False, default=now, verbose_name='Дата добавления')

    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус операции')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, verbose_name='Подкатегория операции')

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

    def __str__(self):
        created_on_date = date.fromisoformat(str(self.created_on))
        return f'Операция ({self.pk}) от {created_on_date.strftime('%d.%m.%Y')}'

