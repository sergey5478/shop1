from django.core.management import BaseCommand

from shopapp.models import Client


class Command(BaseCommand):
    help = "Get client by id."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        client = Client.objects.get(id=id)
        self.stdout.write(f'{client}')
