from django.urls import path

from transactions import autocomplete

urlpatterns = [
    path('subcategory-autocomplete/', autocomplete.SubcategoryAutocomplete.as_view(), name='subcategory-autocomplete'),
    path('category-autocomplete/', autocomplete.CategoryAutocomplete.as_view(), name='category-autocomplete'),
    path('type-autocomplete/', autocomplete.TypeAutocomplete.as_view(), name='type-autocomplete'),
]