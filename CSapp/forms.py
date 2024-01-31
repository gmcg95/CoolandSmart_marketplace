from django import forms
from .models.product import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'available_quantity', 'materials', 'rarity']