from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    help = 'Create product'

    def handle(self, *args, **kwargs):
        for i in range(10):
            product = Product(name_product=f'name_product_{i}',
                              product_description=f'product_description_{i}',
                              price_product=f'price_product_{i}',
                              quantity_product=f'quantity_product_{i}',
                              date_product_added=f'date_product_added_{i}')
            product.save()
        self.stdout.write('product created')
