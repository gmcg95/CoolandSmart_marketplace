from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order
from .forms import OrderItemForm
from django.http import JsonResponse
from products_app.models.product import Product
from django.urls import reverse
from django.db.models import F


# Create your views here.
def home_view(request):
    return render(request, 'CSapp/home.html')


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.status = 'unread'
            new_message.save()
            return redirect('/')  # contact-page (or another page) redirect
    else:
        form = MessageForm()

    return render(request, 'CSapp/contact.html', {'form': form})


@login_required
def add_to_cart(request, product_id):
    try:
        # get item by id
        product = get_object_or_404(Product, id=product_id)

        # check if already exists and OrderItem for this product and user
        order_item, created = OrderItem.objects.get_or_create(
            user=request.user,
            ordered=False,
            product=product
        )

        if created:
            messages.success(request, f"{product.name} was added to cart")
        else:
            # if OrderItem already exists, update quantity
            order_item.quantity = F('quantity') + 1
            order_item.save()
            messages.info(request, f"{product.name} quantity was updated to cart.")

        # redirect to cart
        return redirect(reverse('CSapp:shopping_cart'))
    except Exception as e:
        # error management
        messages.error(request, f"Product add to cart error: {str(e)}")
        return redirect('/')


@login_required
def create_order(request):
    form = OrderItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            product_id = form.cleaned_data['product'].id
            quantity = form.cleaned_data['quantity']

            order_item, created = OrderItem.objects.get_or_create(
                user=request.user,
                ordered=False,
                product_id=product_id,
            )
            order_item.quantity += quantity
            order_item.save()

            return JsonResponse({'status': 'success'})

    order_items = OrderItem.objects.filter(user=request.user, ordered=False)
    order_total = sum(item.get_final_price() for item in order_items)

    context = {
        'form': form,
        'order_items': order_items,
        'order_total': order_total,
    }
    return render(request, 'CSapp/shopping_cart.html', context)


def checkout(request):
    if request.method == 'POST':
        # retrieves un-purchased order items for the logged-in user
        order_items = OrderItem.objects.filter(user=request.user, ordered=False)

        # creates a new order in the database with the items in the cart
        new_order = Order.objects.create(user=request.user, ordered=True)
        new_order.items.set(order_items)

        # update order items status to "ordered"
        order_items.update(ordered=True)

        messages.success(request, 'The order has been successfully placed!')
        return redirect(reverse('CSapp:home'))  # change this redirect to the one you want

    # redirect to another page or return an appropriate response
    return redirect(reverse('CSapp:home'))  # change this redirect to the one you want


def shopping_cart(request):
    # get all un-purchased order items for the logged-in user
    order_items = OrderItem.objects.filter(user=request.user, ordered=False)

    # order total
    order_total = sum(item.get_final_price() for item in order_items)

    context = {
        'order_items': order_items,
        'order_total': order_total,
    }

    return render(request, 'CSapp/shopping_cart.html', context)


@login_required
def delete_product(request, product_id):
    if request.method == 'DELETE':
        try:
            order_item = OrderItem.objects.get(user=request.user, product_id=product_id, ordered=False)
            order_item.delete()
            return JsonResponse({'status': 'success'})
        except OrderItem.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'The products was not found in the cart'})
    else:
        return JsonResponse({'status': 'error', 'message': 'The requested method is not allowed'})





