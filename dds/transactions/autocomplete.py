from dal import autocomplete

from transactions.models import Subcategory, Category, Type


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Category.objects.none()

        qs = Category.objects.all()

        subcategory_id = self.forwarded.get('subcategory')
        type_id = self.forwarded.get('type')

        if subcategory_id:
            selected_subcategory_category_id = Subcategory.objects.get(id=subcategory_id).category_id
            qs = Category.objects.filter(id=selected_subcategory_category_id)
        elif type_id:
            qs = Category.objects.filter(type_id=type_id)

        return qs.order_by('name')


class SubcategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Subcategory.objects.none()

        qs = Subcategory.objects.all()

        category_id = self.forwarded.get('category')
        type_id = self.forwarded.get('type')

        if type_id:
            qs = qs.filter(category__type_id=type_id)
        if category_id:
            qs = qs.filter(category_id=category_id)

        return qs.order_by('name')


class TypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Type.objects.none()

        qs = Type.objects.all()
        subcategory_id = self.forwarded.get('subcategory')
        category_id = self.forwarded.get('category')

        if subcategory_id:
            selected_subcategory_type_id = Subcategory.objects.get(id=subcategory_id).category.type_id
            qs = qs.filter(id=selected_subcategory_type_id)
        elif category_id:
            selected_category_type_id = Category.objects.get(id=category_id).type_id
            qs = qs.filter(id=selected_category_type_id)

        return qs.order_by('name')