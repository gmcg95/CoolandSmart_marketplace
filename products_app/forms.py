# products_app/forms.py
from django import forms
from .models.product import Product
from .models.category import Category
from .models.manufacturer import Manufacturer


class ManufacturerUploadForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name']


class CategoryUploadForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ProductUploadForm(forms.ModelForm):
    EXISTING_CATEGORY_CHOICES = Category.objects.all()
    EXISTING_MANUFACTURER_CHOICES = Manufacturer.objects.all()

    category = forms.ModelChoiceField(queryset=EXISTING_CATEGORY_CHOICES, required=False, label='Category:')
    new_category_name = forms.CharField(max_length=255, required=False, label='New category:')

    manufacturer = forms.ModelChoiceField(queryset=EXISTING_MANUFACTURER_CHOICES, required=False, label='Supplier:')
    new_manufacturer_name = forms.CharField(max_length=255, required=False, label='New supplier:')

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'available_quantity', 'materials', 'rarity',
                  'category', 'manufacturer']