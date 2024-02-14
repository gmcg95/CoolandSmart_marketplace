from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView
from products_app.models.product import Product
from products_app.models.category import Category
from products_app.models.manufacturer import Manufacturer
from products_app.forms import ProductUploadForm, CategoryUploadForm, ManufacturerUploadForm


class ProductListView(ListView):
    model = Product  # Specifies the model for which to display the list
    template_name = 'products_app/products.html'  # specify the associated HTML template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = context['object_list']  # adds a new key in context
        return context


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products_app/product.html', {'product': product})


def upload_manufacturer(request):
    form = ManufacturerUploadForm()

    if request.method == 'POST':
        form = ManufacturerUploadForm(request.POST)
        if form.is_valid():
            form.save()
            form = ManufacturerUploadForm()

    return render(request, 'products_app/upload_manufacturer.html', {'form': form})


def upload_category(request):
    form = CategoryUploadForm()

    if request.method == 'POST':
        form = CategoryUploadForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoryUploadForm()

    return render(request, 'products_app/upload_category.html', {'form': form})


def upload_product(request):
    form = ProductUploadForm()
    categories = Category.objects.all()
    manufacturers = Manufacturer.objects.all()

    if request.method == 'POST':
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.cleaned_data.get('category', None)
            new_category_name = form.cleaned_data.get('new_category_name', None)
            manufacturer = form.cleaned_data.get('manufacturer', None)
            new_manufacturer_name = form.cleaned_data.get('new_manufacturer_name', None)

            # gets the Category object or creates a new one
            if not category and new_category_name:
                category, created = Category.objects.get_or_create(name=new_category_name)

            # gets the Manufacturer object or creates a new one
            if not manufacturer and new_manufacturer_name:
                manufacturer, created = Manufacturer.objects.get_or_create(name=new_manufacturer_name)

            # creates the Product object, distributes and saves the categories for the product
            product = form.save(commit=False)
            product.category = category
            product.manufacturer = manufacturer
            product.save()

            # Form reset if the product upload was successful
            form = ProductUploadForm()

    return render(request, 'products_app/upload_product.html', {'form': form,'categories': categories,
                                                                'manufacturers': manufacturers})

