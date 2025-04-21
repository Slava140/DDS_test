from dal import autocomplete
from django import forms
from transactions.models import Transaction, Category, Type, Subcategory


class TransactionAdminForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,  # Поле обязательно, False чтобы была возможность очистить
        label='Категория',
        widget=autocomplete.ModelSelect2(
            url='category-autocomplete',
            forward=['subcategory', 'type']
        )
    )

    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        required=False,  # Поле обязательно, False чтобы была возможность очистить
        label='Тип',
        widget=autocomplete.ModelSelect2(
            url='type-autocomplete',
            forward=['subcategory', 'category']
        )
    )

    subcategory = forms.ModelChoiceField(
        queryset=Subcategory.objects.all(),
        required=False,  # Поле обязательно, False чтобы была возможность очистить
        label='Подкатегория',
        widget=autocomplete.ModelSelect2(
            url='subcategory-autocomplete',
            forward=['category', 'type']
        )
    )

    class Meta:
        model = Transaction
        fields = ['created_on', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            # Нужно, чтобы при открытии на редактирование отображались текущие данные
            self.fields['category'].initial = self.instance.subcategory.category
            self.fields['type'].initial = self.instance.subcategory.category.type


    def __clean_field(self, field_name: str):
        field = self.cleaned_data.get(field_name)
        if not field:
            raise forms.ValidationError('Обязательное поле.')
        return field

    def clean_type(self): return self.__clean_field('type')
    def clean_category(self): return self.__clean_field('category')
    def clean_subcategory(self): return self.__clean_field('subcategory')
