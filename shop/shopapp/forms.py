from django import forms
import datetime
from . import models


class ClientForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(label='N телефона', max_length=100)
    client_address = forms.CharField(label='Адрес', widget=forms.Textarea)
    customer_registration_date = forms.DateField(label='Дата регистрации', initial=datetime.date.today,
                                                 widget=forms.DateInput(attrs={'type': 'date'}))


class ProductForm(forms.Form):
    name_product = forms.CharField(label='Название', max_length=100)
    product_description = forms.CharField(label='Содержание', widget=forms.Textarea)
    price_product = forms.CharField(label='Цена', max_length=100)
    quantity_product = forms.CharField(label='Количество', max_length=100)
    date_product_added = forms.DateField(label='Дата регистрации', initial=datetime.date.today,
                                         widget=forms.DateInput(attrs={'type': 'date'}))
    image = forms.ImageField(label='Картинка')


class OrderForm(forms.Form):
    order_client = forms.ModelChoiceField(label='Клиент', queryset=models.Client.objects.all())
    order_product = forms.ModelChoiceField(label='Продукт', queryset=models.Product.objects.all())
    total_amount_order = forms.CharField(label='Сумма', max_length=100)
    date_order = forms.DateField(label='Дата регистрации', initial=datetime.date.today,
                                 widget=forms.DateInput(attrs={'type': 'date'}))
