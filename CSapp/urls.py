from django.urls import path
from CSapp.views import home_view, contact, add_to_cart, delete_product, shopping_cart, checkout

app_name = 'CSapp'

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact, name='contact'),
    path('shopping_cart/', shopping_cart, name='shopping_cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('checkout/', checkout, name='checkout'),

    ]
