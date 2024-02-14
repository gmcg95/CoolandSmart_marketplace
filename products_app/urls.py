from django.urls import path
from products_app.views import upload_manufacturer, upload_category, upload_product, product_details, ProductListView


app_name = 'products_app'

urlpatterns = [
    path('upload_manufacturer/', upload_manufacturer, name='upload-manufacturer'),
    path('upload_category/', upload_category, name='upload-category'),
    path('upload_product/', upload_product, name='upload-product'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product/<int:product_id>/', product_details, name='product'),
    # Another URL rules can be added here
]
