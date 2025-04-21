from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from transactions.models import Transaction, Status, Type, Category, Subcategory
from transactions.forms import TransactionAdminForm


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['created_on', 'status_name', 'type_name', 'category_name', 'subcategory_name', 'amount', 'comment']
    list_display_links = ['created_on']
    list_filter = [
        ('created_on', DateRangeFilter),
        'status__name',
        'subcategory__name',
        'subcategory__category__name',
        'subcategory__category__type__name'
    ]
    ordering = ['created_on', 'amount']
    form = TransactionAdminForm

    @admin.display(description='Статус')
    def status_name(self, transaction: Transaction):
        return transaction.status.name

    @admin.display(description='Подкатегория')
    def subcategory_name(self, transaction: Transaction):
        return transaction.subcategory.name

    @admin.display(description='Категория')
    def category_name(self, transaction: Transaction):
        return transaction.subcategory.category.name

    @admin.display(description='Тип')
    def type_name(self, transaction: Transaction):
        return transaction.subcategory.category.type.name


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'type_name']
    list_filter = ['type__name']

    @admin.display(description='Тип')
    def type_name(self, category: Category):
        return category.type.name


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_name', 'type_name']
    list_filter = ['category__name', 'category__type__name']

    @admin.display(description='Категория')
    def category_name(self, subcategory: Subcategory):
        return subcategory.category.name

    @admin.display(description='Тип')
    def type_name(self, subcategory: Subcategory):
        return subcategory.category.type.name