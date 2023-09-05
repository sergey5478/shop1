from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.TextField()
    client_address = models.TextField()
    customer_registration_date = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name_product = models.CharField(max_length=100)
    product_description = models.TextField()
    price_product = models.TextField()
    quantity_product = models.TextField()
    date_product_added = models.DateTimeField(auto_now=True)
    image = models.ImageField()


class Order(models.Model):
    order_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_amount_order = models.IntegerField()
    date_order = models.DateTimeField(auto_now=True)
