from django import forms
from django.forms import ModelForm

from storage.models import Product
from store.models import Category


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price','category','stock','image','brand','is_on_sale','on_sale_price']

    def clean_on_sale_price(self):
        on_sale_price = self.cleaned_data.get('on_sale_price')
        price = self.cleaned_data.get('price')

        if on_sale_price is not None and price is not None:
            if on_sale_price > price:
                raise forms.ValidationError(f"On sale price cannot be greater than original price .")
        return on_sale_price

class CreateNewCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Category.objects.filter(name=name).exists():
            raise forms.ValidationError(f"Category {name} already exists.")
        return name

class EditProductForm(CreateProductForm):
    ...

class EditCategoryForm(CreateNewCategoryForm):
    ...