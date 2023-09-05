from django.core.management import BaseCommand
from shopapp.models import Client


class Command(BaseCommand):
    help = 'Create clients'

    def handle(self, *args, **kwargs):
        for i in range(10):
            client = Client(name=f'name_{i}', email=f'email_{i}@mail.ru',
                            phone_number=f'phone_number_{i}',
                            client_address=f'client_address_{i}',
                            customer_registration_date=f'customer_registration_date_{i}')
            client.save()
        self.stdout.write('client created')