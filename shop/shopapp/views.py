from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from . import forms, models
from .models import Order, Product


def get_orders(request):
    orders = Order.objects.all()
    return render(request, 'shopapp/orders.html', {'orders': orders})


def get_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    client_orders = Order.objects.filter(order_client=order.order_client)
    return render(request, 'shopapp/order_details.html', {'order': order, 'client_orders': client_orders})


def get_ordered_products(request):
    seven_days_ago = timezone.now() - timedelta(days=7)
    thirty_days_ago = timezone.now() - timedelta(days=30)
    year_ago = timezone.now() - timedelta(days=365)

    ordered_products_7_days = Product.objects.filter(order__date_order__gte=seven_days_ago).distinct()
    ordered_products_30_days = Product.objects.filter(order__date_order__gte=thirty_days_ago).distinct()
    ordered_products_365_days = Product.objects.filter(order__date_order__gte=year_ago).distinct()

    context = {
        'ordered_products_7_days': ordered_products_7_days,
        'ordered_products_30_days': ordered_products_30_days,
        'ordered_products_365_days': ordered_products_365_days,
    }

    return render(request, 'shopapp/ordered_products.html', context)


def client_form(request):
    message = ''
    if request.method == 'POST':
        form = forms.ClientForm(request.POST)
        if form.is_valid():
            сlient = models.Client(name=form.cleaned_data['name'],
                                   phone_number=form.cleaned_data['phone_number'],
                                   email=form.cleaned_data['email'],
                                   client_address=form.cleaned_data['client_address'],
                                   customer_registration_date=form.cleaned_data['customer_registration_date'])
            сlient.save()
            message = 'Клиент успешно сохранен'
    else:
        form = forms.ClientForm()

    return render(request, 'shopapp/base.html',
                  {'form': form, 'message': message, 'title': 'Сохранение клинта'})


def product_form(request):
    message = ''
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = models.Product(name_product=form.cleaned_data['name_product'],
                                     product_description=form.cleaned_data['product_description'],
                                     price_product=form.cleaned_data['price_product'],
                                     quantity_product=form.cleaned_data['quantity_product'],
                                     date_product_added=form.cleaned_data['date_product_added'],
                                     image=form.cleaned_data['image'])
            product.save()
            message = 'Продукт успешно сохранен'
    else:
        form = forms.ProductForm()

    return render(request, 'shopapp/image.html',
                  {'form': form, 'message': message, 'title': 'Сохранение продукта'})


def order_form(request):
    message = ''
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            order = models.Order(order_client=form.cleaned_data['order_client'],
                                 order_product=form.cleaned_data['order_product'],
                                 total_amount_order=form.cleaned_data['total_amount_order'],
                                 date_order=form.cleaned_data['date_order'], )
            order.save()
            message = 'Заказ успешно сохранен'
    else:
        form = forms.OrderForm()

    return render(request, 'shopapp/base.html',
                  {'form': form, 'message': message, 'title': 'Сохранение заказа'})


def index(request):
    return render(request, 'shopapp/index.html')