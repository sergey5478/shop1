from django.core.management.base import BaseCommand
from shopapp.models import Order, Client, Product
from datetime import datetime
import random


class Command(BaseCommand):
    help = 'Creates random orders'

    def handle(self, *args, **options):
        """Create clients, products. """
        clients = Client.objects.all()
        products = Product.objects.all()

        num_orders = 10

        for _ in range(num_orders):
            client = random.choice(clients)
            product = random.choice(products)

            total_amount = random.randint(50, 500)
            date_order = datetime.now()

            order = Order(order_client=client,
                          order_product=product,
                          total_amount_order=total_amount,
                          date_order=date_order)
            order.save()

        self.stdout.write(self.style.SUCCESS(f"{num_orders} заказов успешно создано."))
